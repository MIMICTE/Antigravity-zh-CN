# Antigravity-zh-CN

<div align="center">

**🌏 English | [简体中文](README.md)**

An open-source Chinese localization patch for Google Antigravity Desktop

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS-lightgrey.svg)](https://www.microsoft.com/windows)

</div>

---

## 📖 Project Overview

**Antigravity v2.5.0 Chinese Localization Patch** - Provides complete Chinese interface support for Google Antigravity desktop application.

This project uses innovative **Web Injection and Native ASAR Unpacking Technology** to achieve perfect localization without compromising the original software's security and stability.

## ✨ Key Features

- 🚀 **Zero Dependencies** - Built-in pure Python ASAR parser and packer using only `struct` and `json` libraries, no Node.js or npm required
- 🎯 **Smart Text Matching** - Uses low-level `indexOf` fragmentation reconstruction and CSS pseudo-class polymorphic matching to bypass Webpack code splitting issues
- ⚡ **One-Click Deployment** - Automatically handles process cleanup and software restart for a seamless "press Enter → enjoy Chinese" experience
- 🛡️ **Clean & Reversible** - Complete removal of localization with restore script, ensuring "lossless rollback" to official English version at any time
- 🧭 **Cross-Platform Compatibility** - Supports native path resolution for both Windows (`LOCALAPPDATA`) and macOS (`/Applications`).

## 📦 Download & Installation

### Option 1: Python Script Version 

**Download:** [Antigravity-zh-CN-v2.5.0-Windows-x64.zip](https://github.com/MIMICTE/Antigravity-zh-CN/releases/latest) (Note: The .exe is Windows only; macOS users should use the source code/script)

**Features:**
- ✅ Open source and transparent, auditable code
- ✅ Small file size (about 40 KB)
- ✅ Won't be flagged by antivirus software

**Prerequisites:**

Install [Python 3.8 or higher](https://www.python.org/downloads/)
- Make sure to check **"Add Python to PATH"** during installation

**How to use:**
1. Download and extract the ZIP file
2. Double-click `Antigravity-Patcher.py` to apply the patch

The script will automatically:
- Close Antigravity process
- Unpack and inject localization code
- Restart the software with Chinese interface

3. Double-click `Restore.py` to restore to official English version

> 💡 **Tip**: If double-clicking doesn't work, try:
> - Right-click → "Open with" → "Python"
> - Or open command line in the project directory and run:
>   ```bash
>   python3 Antigravity-Patcher.py  # Apply patch (macOS / Linux users should use python3)
>   python3 Restore.py              # Restore English
>   ```

---

### Option 2: Install from Source ⭐ Recommended for Developers

**Clone the repository:**
```bash
git clone https://github.com/MIMICTE/Antigravity-zh-CN.git
cd Antigravity-zh-CN
python3 Antigravity-Patcher.py
```

**Or download source code archive:**

Download `Source code (zip)` or `Source code (tar.gz)` from [Releases page](https://github.com/MIMICTE/Antigravity-zh-CN/releases/latest), extract and run `Antigravity-Patcher.py`.

## 💡 Technical Approach

This project leverages Electron framework mechanisms:

### 1. Unpacked Patching
Disables the official `app.asar` file, forcing the software to read from the unpacked `app` folder with injected localization code.

### 2. Dynamic DOM Interception
Injects `MutationObserver` in `preload.js` to monitor DOM changes in real-time and replace English text with Chinese.

### 3. Native ASAR Parser
Pure Python implementation of ASAR file format parser with zero external dependencies.

## ⚠️ Known Limitations

- **Thought Process in English** - Due to AI model's streaming output architecture, the agent's backend thinking logs (`Thought` process) cannot be localized, but all final responses and frontend UI elements are 100% localized
- **Windows and macOS Only** - Currently optimized for Windows and macOS. Linux support may require manual path adjustments.
- **Version Specific** - Optimized for Antigravity v2.5.0; other versions may require adjustments

## 📸 Screenshots

<div align="center">

![Antigravity Chinese Interface](antigravity-chinese.png)

*Antigravity with Chinese interface - All text fully localized*

</div>

**Fully localized interface includes:**
- ✅ Sidebar menu (New conversation, History, Scheduled tasks, Projects)
- ✅ Top navigation bar (File, Audio, Window)
- ✅ Input placeholder text and model selector
- ✅ Settings page with all options and descriptions

> 💡 Tip: To see the actual result, simply double-click `Antigravity-Patcher.py` or `Antigravity-Patcher.exe` to experience the complete Chinese interface!

## 🔐 Security

This project is completely open-source and secure:

### ✅ What We Do

- **UI Text Only** - Only replaces display text at the frontend level, no network interception, data collection, or account access
- **Open Source** - All code is fully open-source with no obfuscation, encryption, or hidden logic
- **Reversible** - Complete restore mechanism, one-click rollback to original version
- **Zero External Dependencies** - Pure Python standard library implementation, no external server connections

### 🛡️ How It Works

1. **ASAR Unpacking** - Pure Python parser for Electron's ASAR package format
2. **Code Injection** - Append translation code to `preload.js` and `menu.js`
3. **DOM Monitoring** - Use `MutationObserver` to watch page changes
4. **Text Replacement** - Dictionary-based English to Chinese text replacement

### About the .exe Version

- .exe files are packaged using [PyInstaller](https://pyinstaller.org/) open-source tool
- Contains complete Python runtime environment (hence larger file size ~7-8 MB)
- May be flagged by some antivirus software, which is a known PyInstaller issue
- If you have security concerns, use the Python script version (completely transparent code)

No reverse engineering or cracking involved.

## ❓ FAQ

<details>
<summary><b>Q: What's the difference between Python script and .exe versions?</b></summary>

A: 
- **Python script version**: Requires Python environment, small size, transparent code
- **.exe version**: No Python needed, ready to use, but larger file size and may trigger false positives

Both versions have identical functionality. Choose based on your technical comfort level.
</details>

<details>
<summary><b>Q: Why is the .exe file so large?</b></summary>

A: The .exe file includes the complete Python runtime environment, so ~7-8 MB is normal.
</details>

<details>
<summary><b>Q: Antivirus flagging as virus?</b></summary>

A: This is a known PyInstaller issue, not an actual virus. You can:
- Add to antivirus whitelist
- Use Python script version instead (recommended)
- Upload to [VirusTotal](https://www.virustotal.com/) for verification
</details>

<details>
<summary><b>Q: "Python is not recognized as an internal or external command"?</b></summary>

A: Python is not added to your system PATH. Reinstall Python and make sure to check "Add Python to PATH" during installation.
</details>

<details>
<summary><b>Q: Software won't start after applying the patch?</b></summary>

A: Try these steps:
1. Run `Restore.py` or `Restore.exe` to restore original version
2. Ensure the original Antigravity works properly
3. Check if antivirus software is blocking the script
4. Run the script as administrator
</details>

<details>
<summary><b>Q: Some parts of the UI are still in English?</b></summary>

A: This is normal. Some content cannot be localized because:
- AI thinking logs (Thought) must remain in English for model stability
- Dynamically generated content may not be covered by the dictionary
- Feel free to submit an Issue to report missing translations
</details>

<details>
<summary><b>Q: Localization stops working after software update?</b></summary>

A: Antigravity updates may overwrite localization files. Please:
1. Run `Restore.py` or `Restore.exe` to clean up old version
2. Wait for this project to update for the new version
3. Or re-run the patch script on the new version (may be unstable)
</details>

<details>
<summary><b>Q: Does this patch affect software security?</b></summary>

A: No. This patch only modifies UI text display and does not involve network communication, data encryption, account authentication, or core functionality. All changes are at the frontend level and do not affect communication with servers.
</details>

<details>
<summary><b>Q: How to add new translations?</b></summary>

A: Edit the `dictionary` in `Antigravity-Patcher.py` and add key-value pairs:
```python
"English Text": "中文翻译",
```
Then re-run the patch script.
</details>

<details>
<summary><b>Q: Does it support other operating systems?</b></summary>

A: Currently, Windows and macOS are supported. Linux versions may require path modifications.
</details>

More questions? Welcome to ask in [GitHub Issues](../../issues) or [Discussions](../../discussions)!

## 🤝 Contributing

Issues and Pull Requests are welcome!

- Found translation errors or omissions? Submit an [Issue](../../issues) or PR
- Have better technical solutions? Discuss in [Discussions](../../discussions)

For detailed contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## ⚠️ Disclaimer

- This project is for educational purposes only
- Users are responsible for any issues arising from using this patch
- Please use official licensed Antigravity software
- Please comply with Antigravity's Terms of Service

## 🌟 Star History

If this project helps you, please consider giving it a star ⭐️

## 📧 Contact

- Issues: [GitHub Issues](../../issues)
- Discussions: [GitHub Discussions](../../discussions)

---

<div align="center">

**Made with ❤️ by Antigravity-zh-CN Contributors**

</div>
