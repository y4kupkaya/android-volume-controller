#!/usr/bin/env python3
"""
Android Volume Controller for Windows
Control your Android device's volume directly from Windows Volume Mixer

Copyright (C) 2025 Yakup Kaya (y4kupkaya@github) - yakupkaya.me

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

import re
import subprocess
import time
import threading
import os
import sys
import wave
import struct
import logging
import signal
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class DependencyError(Exception):
    """Raised when required dependencies are not available"""

    pass


class AndroidDeviceError(Exception):
    """Raised when Android device connection issues occur"""

    pass


class AudioSystemError(Exception):
    """Raised when audio system initialization fails"""

    pass


class AndroidVolumeController:
    """
    Main controller class for managing Android device volume through Windows Volume Mixer.

    This class handles:
    - ADB communication with Android devices
    - Windows audio system integration
    - Volume synchronization between Windows and Android
    - Audio session management
    """

    def __init__(self, background_mode=False, verbose=False):
        """Initialize the Android Volume Controller."""
        self.adb_path = "adb"  # Assumes adb is in system PATH
        self.android_max_volume = 0
        self.last_android_volume = -1
        self.last_mute_state = False
        self.running = True
        self.audio_thread = None
        self.connection_lost = False
        self.background_mode = background_mode
        self.verbose = verbose

        # Configure logging based on mode
        if self.background_mode:
            logging.getLogger().setLevel(logging.ERROR)
        elif self.verbose:
            logging.getLogger().setLevel(logging.DEBUG)
        
        # Set up signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

        if not self.background_mode:
            logger.info("Initializing Android Volume Controller")

        try:
            self._check_dependencies()
            self._initialize_android_connection()
            self._start_audio_system()
        except (DependencyError, AndroidDeviceError, AudioSystemError) as e:
            logger.error(f"Initialization failed: {e}")
            sys.exit(1)

    def _signal_handler(self, signum, frame):
        """Handle system signals for graceful shutdown."""
        if not self.background_mode:
            logger.info("Received shutdown signal, cleaning up...")
        self.cleanup()
        sys.exit(0)

    def _check_dependencies(self):
        """
        Check if all required dependencies are available.

        Raises:
            DependencyError: If required dependencies are missing
        """
        if not self.background_mode:
            logger.info("Checking system dependencies...")

        # Check pycaw library
        try:
            from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

            self.AudioUtilities = AudioUtilities
            self.ISimpleAudioVolume = ISimpleAudioVolume
            if not self.background_mode:
                logger.info("✓ pycaw library available")
        except ImportError as e:
            raise DependencyError(
                "pycaw library is required but not installed. "
                "Please install it using: pip install pycaw"
            ) from e

        # Check winsound (should be built-in on Windows)
        try:
            import winsound

            self.winsound = winsound
            if not self.background_mode:
                logger.info("✓ winsound module available")
        except ImportError as e:
            raise DependencyError(
                "winsound module is not available. "
                "This application requires Windows OS."
            ) from e

        # Check ADB availability
        try:
            result = subprocess.run(
                [self.adb_path, "version"], capture_output=True, text=True, timeout=5
            )
            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, "adb version")
            if not self.background_mode:
                logger.info("✓ ADB is installed and accessible")
        except (
            subprocess.CalledProcessError,
            subprocess.TimeoutExpired,
            FileNotFoundError,
        ) as e:
            raise DependencyError(
                "ADB (Android Debug Bridge) is required but not accessible. "
                "Please install Android SDK Platform Tools and add it to your PATH."
            ) from e

    def _initialize_android_connection(self):
        """
        Initialize connection with Android device and get volume information.

        Raises:
            AndroidDeviceError: If device connection fails
        """
        if not self.background_mode:
            logger.info("Initializing Android device connection...")

        # Check for connected devices
        try:
            result = subprocess.run(
                [self.adb_path, "devices"], capture_output=True, text=True, timeout=5
            )

            if result.returncode != 0:
                raise subprocess.CalledProcessError(result.returncode, "adb devices")

            devices = [line for line in result.stdout.split("\n") if "\tdevice" in line]

            if not devices:
                raise AndroidDeviceError(
                    "No Android device found. Please ensure:\n"
                    "• Device is connected via USB\n"
                    "• USB Debugging is enabled in Developer Options\n"
                    "• Computer is authorized on the device"
                )

            device_id = devices[0].split("\t")[0]
            if not self.background_mode:
                logger.info(f"✓ Android device connected: {device_id}")

        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            raise AndroidDeviceError(f"Failed to check device connection: {e}") from e

        # Get maximum volume level
        self.android_max_volume = self._get_android_max_volume()
        if self.android_max_volume <= 0:
            raise AndroidDeviceError("Failed to retrieve device volume information")

        if not self.background_mode:
            logger.info(f"✓ Android maximum volume level: {self.android_max_volume}")

    def _get_android_max_volume(self):
        """
        Retrieve the maximum volume level from Android device.

        Returns:
            int: Maximum volume level for STREAM_MUSIC
        """
        try:
            result = subprocess.run(
                [self.adb_path, "shell", "dumpsys", "audio"],
                capture_output=True,
                text=True,
                timeout=10,
            )

            if result.returncode != 0:
                logger.warning("Failed to get volume info from dumpsys, using fallback")
                return 25  # Fallback value

            output = result.stdout

            # Search for STREAM_MUSIC maximum volume patterns
            patterns = [
                r"STREAM_MUSIC.*?indexMax:\s*(\d+)",
                r"STREAM_MUSIC.*?Max:\s*(\d+)",
                r"- STREAM_MUSIC.*?(\d+)",
            ]

            for pattern in patterns:
                match = re.search(pattern, output, re.DOTALL | re.IGNORECASE)
                if match:
                    max_volume = int(match.group(1))
                    if max_volume > 0:
                        return max_volume

        except (
            subprocess.CalledProcessError,
            subprocess.TimeoutExpired,
            ValueError,
        ) as e:
            logger.warning(f"Error retrieving Android volume info: {e}")

        # Return reasonable fallback if detection fails
        return 25

    def _set_android_volume(self, volume_level):
        """
        Set the Android device volume level.

        Args:
            volume_level (int): Target volume level

        Returns:
            bool: True if successful, False otherwise
        """
        if self.connection_lost:
            return False

        try:
            # Primary method using media_session
            result = subprocess.run(
                [
                    self.adb_path,
                    "shell",
                    "cmd",
                    "media_session",
                    "volume",
                    "--stream",
                    "3",
                    "--set",
                    str(int(volume_level)),
                ],
                capture_output=True,
                timeout=3,
            )

            if result.returncode == 0:
                return True
            else:
                # Fallback method using service call
                return self._set_android_volume_fallback(volume_level)

        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            logger.warning(f"Volume set failed, trying fallback: {e}")
            return self._set_android_volume_fallback(volume_level)

    def _set_android_volume_fallback(self, volume_level):
        """
        Fallback method for setting Android volume using service call.

        Args:
            volume_level (int): Target volume level

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            subprocess.run(
                [
                    self.adb_path,
                    "shell",
                    "service",
                    "call",
                    "audio",
                    "3",
                    "i32",
                    "3",
                    "i32",
                    str(int(volume_level)),
                    "i32",
                    "1",
                ],
                capture_output=True,
                timeout=3,
            )
            return True
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            logger.error(f"Fallback volume set also failed: {e}")
            self._handle_connection_loss()
            return False

    def _set_android_mute(self, mute_state):
        """
        Set the Android device mute state.

        Args:
            mute_state (bool): True to mute, False to unmute

        Returns:
            bool: True if successful, False otherwise
        """
        if self.connection_lost:
            return False

        try:
            if mute_state:
                # Mute by setting volume to 0
                cmd = [
                    self.adb_path,
                    "shell",
                    "cmd",
                    "media_session",
                    "volume",
                    "--stream",
                    "3",
                    "--set",
                    "0",
                ]
            else:
                # Unmute by restoring previous volume or setting to 1/3 of max
                target_volume = max(
                    1,
                    (
                        self.last_android_volume
                        if self.last_android_volume > 0
                        else self.android_max_volume // 3
                    ),
                )
                cmd = [
                    self.adb_path,
                    "shell",
                    "cmd",
                    "media_session",
                    "volume",
                    "--stream",
                    "3",
                    "--set",
                    str(int(target_volume)),
                ]

            result = subprocess.run(cmd, capture_output=True, timeout=3)

            if result.returncode == 0:
                return True
            else:
                return self._set_android_mute_fallback(mute_state)

        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            logger.warning(f"Mute operation failed, trying fallback: {e}")
            return self._set_android_mute_fallback(mute_state)

    def _set_android_mute_fallback(self, mute_state):
        """
        Fallback method for muting/unmuting using keyevents.

        Args:
            mute_state (bool): True to mute, False to unmute

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            if mute_state:
                keyevent = "KEYCODE_VOLUME_MUTE"
            else:
                keyevent = "KEYCODE_VOLUME_UP"

            subprocess.run(
                [self.adb_path, "shell", "input", "keyevent", keyevent],
                capture_output=True,
                timeout=3,
            )
            return True
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            logger.error(f"Fallback mute operation also failed: {e}")
            self._handle_connection_loss()
            return False

    def _handle_connection_loss(self):
        """Handle Android device connection loss."""
        if not self.connection_lost:
            self.connection_lost = True
            logger.error("Android device connection lost!")
            logger.error("Please check device connection and restart the application.")
            self.running = False

    def _create_silence_audio_file(self):
        """
        Create a silent WAV file for audio system registration.

        Returns:
            str or None: Path to created file, or None if creation failed
        """
        try:
            silence_file = "controller_silence.wav"

            with wave.open(silence_file, "w") as wav_file:
                wav_file.setnchannels(2)  # Stereo
                wav_file.setsampwidth(2)  # 16-bit
                wav_file.setframerate(44100)  # 44.1kHz

                # Generate 1 second of very low volume audio
                duration = 1
                frames = 44100 * duration
                low_volume_data = []

                for i in range(frames):
                    # Very low amplitude sine wave to ensure audio system recognition
                    sample = int(32 * (i % 100 < 1))
                    low_volume_data.extend([sample, sample])  # Stereo

                wav_data = struct.pack(
                    "<" + "h" * len(low_volume_data), *low_volume_data
                )
                wav_file.writeframes(wav_data)

            return silence_file
        except Exception as e:
            logger.error(f"Failed to create audio file: {e}")
            return None

    def _start_audio_system(self):
        """
        Initialize the audio system for Windows Volume Mixer integration.

        Raises:
            AudioSystemError: If audio system initialization fails
        """
        if not self.background_mode:
            logger.info("Starting audio system...")

        silence_file = self._create_silence_audio_file()
        if not silence_file:
            raise AudioSystemError(
                "Failed to create audio file for system registration"
            )

        def audio_loop():
            """Audio playback loop running in separate thread."""
            self._audio_playback_loop(silence_file)

        self.audio_thread = threading.Thread(target=audio_loop, daemon=True)
        self.audio_thread.start()

        if not self.background_mode:
            logger.info("✓ Audio system started successfully")
            logger.info("Waiting for Windows Volume Mixer registration...")
        time.sleep(3)

    def _audio_playback_loop(self, silence_file):
        """
        Main audio playback loop.

        Args:
            silence_file (str): Path to the silence audio file
        """
        silence_path = os.path.abspath(silence_file)

        try:
            while self.running:
                try:
                    # Play silent audio to maintain Volume Mixer presence
                    self.winsound.PlaySound(
                        silence_path,
                        self.winsound.SND_FILENAME | self.winsound.SND_ASYNC,
                    )
                    time.sleep(3)
                except Exception as e:
                    logger.warning(f"Audio playback error: {e}")
                    time.sleep(1)
        except Exception as e:
            logger.error(f"Audio loop error: {e}")

    def _find_audio_session(self):
        """
        Find the audio session corresponding to this controller in Windows Volume Mixer.

        Returns:
            tuple: (session, volume_interface) if found, (None, None) otherwise
        """
        try:
            sessions = self.AudioUtilities.GetAllSessions()

            target_process_names = [
                "python",
                "controller",
                "android",
            ]

            for session in sessions:
                if session.Process and session.Process.name():
                    process_name = session.Process.name().lower()

                    for target in target_process_names:
                        if target in process_name:
                            try:
                                volume_interface = session._ctl.QueryInterface(
                                    self.ISimpleAudioVolume
                                )
                                return session, volume_interface
                            except Exception:
                                continue

            return None, None
        except Exception as e:
            logger.error(f"Error finding audio session: {e}")
            return None, None

    def start_volume_synchronization(self):
        """
        Start the main volume synchronization loop.

        This method monitors the Windows Volume Mixer for changes and synchronizes
        them with the connected Android device.
        """
        if not self.background_mode:
            logger.info("Starting volume synchronization...")
            logger.info("Instructions:")
            logger.info(
                "1. Open Windows Volume Mixer (right-click speaker icon > Open Volume mixer)"
            )
            logger.info("2. Find 'Python' application in the mixer")
            logger.info("3. Adjust the volume slider to control your Android device")
            logger.info("4. Use mute button to mute/unmute your Android device")
            print("=" * 60)

        audio_session = None
        volume_interface = None
        search_attempts = 0

        while self.running and not self.connection_lost:
            try:
                # Periodically search for audio session
                if audio_session is None or search_attempts % 50 == 0:
                    audio_session, volume_interface = self._find_audio_session()

                    if audio_session and search_attempts == 0 and not self.background_mode:
                        logger.info("✓ Audio session found in Volume Mixer")
                        logger.info(
                            "You can now control your Android device volume from Windows!"
                        )
                    elif audio_session is None and search_attempts % 50 == 0 and not self.background_mode:
                        logger.info("Searching for audio session in Volume Mixer...")

                search_attempts += 1

                # Process volume changes
                if volume_interface:
                    self._process_volume_changes(volume_interface)

                time.sleep(0.1)

            except KeyboardInterrupt:
                logger.info("Received keyboard interrupt")
                break
            except Exception as e:
                logger.error(f"Synchronization error: {e}")
                time.sleep(1)

    def _process_volume_changes(self, volume_interface):
        """
        Process volume and mute state changes from Windows Volume Mixer.

        Args:
            volume_interface: Windows audio volume interface
        """
        try:
            current_volume = volume_interface.GetMasterVolume()
            is_muted = volume_interface.GetMute()

            # Handle mute state changes
            if is_muted != self.last_mute_state:
                self.last_mute_state = is_muted

                if is_muted:
                    if self._set_android_mute(True):
                        if not self.background_mode:
                            logger.info(
                                "🔇 Android device muted (synchronized with Windows)"
                            )
                    else:
                        logger.error("Failed to mute Android device")
                else:
                    if self._set_android_mute(False):
                        if not self.background_mode:
                            logger.info(
                                "🔊 Android device unmuted (synchronized with Windows)"
                            )
                    else:
                        logger.error("Failed to unmute Android device")

            # Handle volume level changes (when not muted)
            if not is_muted:
                android_volume = round(current_volume * self.android_max_volume)

                if android_volume != self.last_android_volume:
                    if self._set_android_volume(android_volume):
                        self.last_android_volume = android_volume
                        if not self.background_mode:
                            percentage = int(current_volume * 100)
                            logger.info(
                                f"📱 Volume updated: {android_volume}/{self.android_max_volume} ({percentage}%)"
                            )
                    else:
                        logger.error(
                            f"Failed to update Android volume to {android_volume}"
                        )

        except Exception as e:
            logger.error(f"Error processing volume changes: {e}")

    def cleanup(self):
        """Perform cleanup operations before shutdown."""
        if not self.background_mode:
            logger.info("Shutting down Android Volume Controller...")
        self.running = False

        # Wait for audio thread to finish
        if self.audio_thread and self.audio_thread.is_alive():
            try:
                self.audio_thread.join(timeout=2)
                if not self.background_mode:
                    logger.info("✓ Audio thread stopped")
            except Exception:
                pass

        # Clean up temporary files
        try:
            temp_files = ["controller_silence.wav"]
            for temp_file in temp_files:
                if os.path.exists(temp_file):
                    os.remove(temp_file)
            if not self.background_mode:
                logger.info("✓ Temporary files cleaned up")
        except Exception as e:
            logger.warning(f"Cleanup warning: {e}")


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Android Volume Controller for Windows",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python android_volume_controller.py              # Normal mode with full output
  python android_volume_controller.py --verbose    # Verbose mode with debug info
  python android_volume_controller.py --background # Background mode (minimal output)

For more information, visit: https://github.com/y4kupkaya/android-volume-controller
        """
    )
    
    parser.add_argument(
        "--background",
        action="store_true",
        help="Run in background mode with minimal console output (errors only)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging with debug information"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="Android Volume Controller v1.0.0"
    )
    
    return parser.parse_args()


def display_welcome_message(background_mode=False):
    """Display welcome message and application information."""
    if not background_mode:
        print("=" * 60)
        print("Android Volume Controller for Windows")
        print("Control your Android device volume from Windows Volume Mixer")
        print("")
        print("Copyright (C) 2025 Yakup Kaya - yakupkaya.me")
        print("Licensed under GNU General Public License v3.0")
        print("=" * 60)


def main():
    """Main application entry point."""
    args = parse_arguments()
    
    # Display welcome message unless in background mode
    display_welcome_message(args.background)
    
    # Show mode info
    if args.verbose and not args.background:
        logger.info("Running in verbose mode")
    elif args.background:
        logger.error("Running in background mode (minimal output)")

    controller = None
    try:
        controller = AndroidVolumeController(
            background_mode=args.background,
            verbose=args.verbose
        )
        controller.start_volume_synchronization()
    except KeyboardInterrupt:
        if not args.background:
            logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 1
    finally:
        if controller:
            controller.cleanup()
        if not args.background:
            logger.info("Application shutdown complete")

    return 0


if __name__ == "__main__":
    sys.exit(main())
