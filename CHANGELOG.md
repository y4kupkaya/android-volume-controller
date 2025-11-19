# Changelog

All notable changes to Android Volume Controller will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Individual app volume control for Android
- Wireless connection support via WiFi
- GUI interface for easier usage
- iOS device support
- Bi-directional volume synchronization

## [1.0.0] - 2025-11-19

### Added
- 🎵 **Core Functionality**
  - Real-time volume synchronization between Windows Volume Mixer and Android devices
  - Windows Audio Session API integration for native volume mixer presence
  - ADB (Android Debug Bridge) communication for Android device control
  - Support for volume range mapping between Windows (0-100%) and Android native ranges

- 🔊 **Audio Features**
  - Mute/unmute functionality with state synchronization
  - Fallback methods for volume control (media_session and service call)
  - Silent audio playback for Windows Volume Mixer registration
  - Smart volume restoration after unmuting

- 📱 **Device Support**
  - Multi-device detection and automatic connection
  - Support for Android 5.0+ devices
  - Compatibility with major Android manufacturers (Samsung, Google, OnePlus, Xiaomi)
  - USB debugging integration

- 🛡️ **Error Handling & Reliability**
  - Comprehensive error handling for connection issues
  - Graceful recovery from temporary disconnections
  - Connection loss detection and user notification
  - Timeout handling for ADB operations

- 🖥️ **Windows Integration**
  - Native Windows Volume Mixer integration
  - Process-based audio session identification
  - Graceful shutdown with signal handling
  - Memory-efficient operation

- 📚 **Documentation**
  - Comprehensive README in English and Turkish
  - Step-by-step installation and setup guides
  - Troubleshooting section with common issues
  - Contributing guidelines for developers
  - Security policy and vulnerability reporting

- 🔧 **Developer Tools**
  - Professional logging system with multiple levels
  - Clean code structure with proper exception handling
  - GPL v3.0 licensing for open source compliance
  - Comprehensive docstrings and code comments

### Technical Details
- **Language**: Python 3.7+
- **Dependencies**: pycaw (Windows audio integration), winsound (built-in)
- **Platform**: Windows 10/11
- **Architecture**: Single-threaded main loop with audio thread
- **Communication**: USB-based ADB protocol

### Security
- Local-only communication via USB
- No internet connectivity required
- Minimal permission requirements (USB debugging only)
- No user data collection or storage
- Open source codebase for transparency

---

## Release Notes Format

### Types of Changes
- **Added** for new features
- **Changed** for changes in existing functionality  
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes

### Versioning
- **Major** (X.0.0): Breaking changes or major new features
- **Minor** (1.X.0): New features, backward compatible
- **Patch** (1.0.X): Bug fixes, backward compatible

[Unreleased]: https://github.com/y4kupkaya/android-volume-controller/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/y4kupkaya/android-volume-controller/releases/tag/v1.0.0