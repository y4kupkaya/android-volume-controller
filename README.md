# 🎵 Android Volume Controller for Windows

**🌍 [Türkçe](README-TR.md) | English**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)
[![ADB](https://img.shields.io/badge/Requires-ADB-green.svg)](https://developer.android.com/studio/command-line/adb)

> 🚀 **Control your Android device's volume directly from Windows Volume Mixer!** 

Transform your Windows PC into a remote control for your Android device's audio system. This innovative application creates seamless integration between Windows Volume Mixer and your Android device, allowing you to adjust volume and mute settings without touching your phone.

## ✨ Features

- 🎛️ **Windows Volume Mixer Integration** - Control Android volume through native Windows interface
- 🔊 **Real-time Volume Synchronization** - Instant volume changes with zero lag
- 🔇 **Mute/Unmute Support** - Complete mute control from Windows
- 📱 **Multi-device Ready** - Automatically detects connected Android devices
- 🛡️ **Robust Error Handling** - Graceful handling of connection issues
- 🔄 **Auto-reconnection** - Smart recovery from temporary disconnections
- 💾 **Memory Efficient** - Minimal system resource usage
- 🎯 **Precise Control** - Full range volume control (0-100%)

## 🎯 How It Works

1. **🔌 Device Connection**: Connects to your Android device via ADB (USB Debugging)
2. **🎵 Audio Registration**: Creates a virtual audio session in Windows Volume Mixer
3. **🔄 Real-time Sync**: Monitors Windows volume changes and applies them to Android
4. **📊 Smart Mapping**: Intelligently maps Windows volume range to Android's native range

## 📋 Prerequisites

### System Requirements
- 🖥️ **Operating System**: Windows 10/11
- 🐍 **Python**: 3.7 or higher
- 📱 **Android Device**: Android 5.0+ with USB Debugging enabled

### Required Tools
- **Android SDK Platform Tools** (for ADB)
- **Python Libraries**: `pycaw` (automatically installed)

## 🚀 Quick Start

### 1. 📥 Installation

```bash
# Clone the repository
git clone https://github.com/y4kupkaya/android-volume-controller.git
cd android-volume-controller

# Install Python dependencies
pip install pycaw
```

### 2. 🔧 Setup Android Device

1. **Enable Developer Options**:
   - Go to `Settings` → `About Phone`
   - Tap `Build Number` 7 times
   
2. **Enable USB Debugging**:
   - Go to `Settings` → `Developer Options`
   - Enable `USB Debugging`
   
3. **Connect Device**:
   - Connect via USB cable
   - Allow USB debugging when prompted

### 3. 🛠️ Setup ADB (Android Debug Bridge)

**Option A: Android Studio (Recommended)**
```bash
# Download Android Studio and install SDK Platform Tools
# Add to PATH: C:\Users\YourUser\AppData\Local\Android\Sdk\platform-tools
```

**Option B: Standalone ADB**
```bash
# Download platform-tools from Google
# Extract and add to Windows PATH
```

**Verify Installation**:
```bash
adb devices
# Should show your connected device
```

### 4. ▶️ Run the Application

```bash
python android_volume_controller.py
```

### 5. 🎛️ Control Volume

1. **Open Windows Volume Mixer**:
   - Right-click speaker icon in system tray
   - Select "Open Volume Mixer"
   
2. **Find Python Application**:
   - Look for "Python" in the volume mixer
   
3. **Control Your Android**:
   - 🔊 Adjust the slider to change Android volume
   - 🔇 Click mute button to mute/unmute Android device

## 🎮 Usage Examples

### Basic Volume Control
```python
# The application runs automatically once started
# Simply use Windows Volume Mixer to control your Android device
```

### Running the Application
```bash
# Start the volume controller
python android_volume_controller.py
```

## 🔧 Configuration

The application automatically detects and configures most settings, but you can customize:

- **Volume Range Mapping**: Automatically adapts to your device's volume range
- **Connection Timeout**: Smart retry mechanism for connection issues
- **Audio Quality**: Optimized for minimal latency

## 📱 Supported Devices

✅ **Tested and Compatible**:
- Samsung Galaxy series
- Google Pixel series
- OnePlus devices
- Xiaomi/MIUI devices
- Most Android 5.0+ devices

⚠️ **Known Limitations**:
- Some custom ROMs may require additional permissions
- Devices with heavily modified audio systems may need manual configuration

## 🐛 Troubleshooting

### Common Issues

**🔴 "No Android device found"**
```bash
# Check device connection
adb devices

# Ensure USB debugging is enabled
# Try different USB cable/port
```

**🔴 "ADB not found"**
```bash
# Install Android SDK Platform Tools
# Add ADB to Windows PATH
# Restart command prompt
```

**🔴 "Audio session not found"**
- Wait a few seconds for Windows to register the audio session
- Check Windows Volume Mixer manually
- Restart the application

**🔴 "Permission denied"**
- Re-authorize USB debugging on Android device
- Check USB connection mode (should be "File Transfer" or "PTP")

### Debug Mode
```bash
# Run with detailed logging
python android_volume_controller.py --debug
```

## 🛡️ Security & Privacy

- 🔒 **Local Connection Only**: All communication happens locally via USB
- 🚫 **No Internet Required**: No data transmitted over the internet
- 🔐 **Minimal Permissions**: Only requires USB debugging access
- 📊 **No Data Collection**: No user data is collected or stored

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 **Fork the Repository**
2. 🌟 **Create a Feature Branch** (`git checkout -b feature/amazing-feature`)
3. 💻 **Make Your Changes**
4. 🧪 **Test Thoroughly**
5. 📝 **Commit Changes** (`git commit -m 'Add amazing feature'`)
6. 🚀 **Push to Branch** (`git push origin feature/amazing-feature`)
7. 🎯 **Open a Pull Request**

### Development Setup
```bash
# Clone for development
git clone https://github.com/y4kupkaya/android-volume-controller.git
cd android-volume-controller

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest tests/
```

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the [LICENSE](LICENSE) file for details.

```
Copyright (C) 2025 Yakup Kaya (y4kupkaya@github)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
```

## 👨‍💻 Author

**Yakup Kaya** 
- 🌐 Website: [yakupkaya.me](https://yakupkaya.me)
- 📧 GitHub: [@y4kupkaya](https://github.com/y4kupkaya)
- 💼 LinkedIn: [Connect with me](https://linkedin.com/in/y4kupkaya)

## 🙏 Acknowledgments

- 📚 **pycaw library** - Windows audio system integration
- 🤖 **Android Debug Bridge** - Android device communication
- 🎵 **Windows Audio Session API** - Volume mixer integration
- 🌟 **Open Source Community** - Inspiration and support

## 🔮 Roadmap

- [ ] 🎚️ **Individual App Control** - Control specific app volumes on Android
- [ ] 🔊 **Audio Profile Management** - Save and load custom audio profiles
- [ ] 📡 **Wireless Support** - Control over WiFi network
- [ ] 🎯 **GUI Interface** - User-friendly graphical interface
- [ ] 📱 **iOS Support** - Extend support to iOS devices
- [ ] 🔄 **Bi-directional Sync** - Sync Android changes back to Windows

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=y4kupkaya/android-volume-controller&type=Date)](https://star-history.com/#y4kupkaya/android-volume-controller&Date)

---

<div align="center">

**Made with ❤️ by [Yakup Kaya](https://yakupkaya.me)**

</div>