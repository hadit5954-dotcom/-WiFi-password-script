# WiFi Password Recovery Script 🔑

A simple Python script to recover and save all saved WiFi passwords on Windows system

---

## 🚀 Features

- 🔍 Automatically detect all saved WiFi profiles
- 🔑 Extract passwords for each network
- 💾 Save results in `wifi_passwords.txt` file
- 📂 Save output file in the same folder as script or executable
- ⚡ Fast and easy to use

---

## 📋 Requirements

- **Windows operating system** (uses `netsh` command)
- **Python 3.x** (when executed as `.py` file)
- No external libraries required (uses only standard library)

---

## 🛠️ Installation and setup

### Method 1: Run as Python script
```bash
git clone https://github.com/hadit5954-dotcom/WiFi-Password-Script.git
cd WiFi-Password-Script
python wifi_passwords.py


Create an executable file (no need for Python)

bash:

pip install pyinstaller
pyinstaller --onefile --console wifi_passwords.py
Then run the wifi_passwords.exe file from the dist folder.


⚠️ Important Notes
Requires Administrator access to access WiFi passwords

Only works for networks you have previously connected to

The netsh command is Windows-specific, so this script only works on Windows


🚀 How it works
Run the command netsh wlan show profiles to get all saved networks

For each profile, run netsh wlan show profile name="..." key=clear

Extract the Key Content (password) field

Save all data in wifi_passwords.txt in the same folder

🔒 Disclaimer
For educational purposes only
This script is designed for personal use to recover your own WiFi passwords. Use only on systems that you own or have permission to access. Unauthorized access to other people's networks is illegal and unethical.

🌟 Give a star
If this project was useful to you, please give it a ⭐!



