# Privacy Settings Analysis Script for Facebook SDKs

This repository contains a Frida script designed to analyze the privacy-related settings and detect the presence of Facebook SDKs within Android applications. The script hooks into various methods provided by Facebook SDKs to retrieve and log information about data collection, privacy preferences, and SDK initialization status.

## Features

- Detects Facebook Core and Audience Network SDK integration.
- Logs key privacy settings like:
  - `getAutoLogAppEventsEnabled`
  - `getAdvertiserIDCollectionEnabled`
  - `getCodelessDebugLogEnabled`
  - `setDataProcessingOptions`
- Monitors changes to privacy settings (`setAutoInitEnabled`, `setMixedAudience`, etc.).
- Handles both getter and setter methods.
- Outputs results in a JSON-like format for easy parsing.

---

## Requirements

1. **Frida**: Ensure that Frida is installed on your system.
   - **Recommended Version**: The script is tested with **Frida 14.2.18**. Using this version is strongly encouraged for compatibility.
   - Installation guide: [Frida Documentation](https://frida.re/docs/installation/)
2. **Rooted Device or Emulator**: Required to inject the script into the target application.
3. **ADB (Android Debug Bridge)**: Ensure ADB is installed and configured.

---

## Usage

### Step 1: Set Up Your Environment

- Ensure the application under analysis is installed on the Android device or emulator.
- Connect the Android device via USB or ensure the emulator is running.

### Step 2: Start Frida Server on the Device

1. Push the Frida server to the device:
   ```bash
   adb push frida-server /data/local/tmp/frida-server
   adb shell chmod +x /data/local/tmp/frida-server
   adb shell /data/local/tmp/frida-server &
    ```
2. Verify the connection:
    ```bash
    frida-ps -U
    ```
3. Inject the Script:
Run the Frida script against the target application using the following command:
    ```bash
    frida -U -n <target_app_package_name> -s privacy_settings_frida.js 
    ```
   
Replace ```<target_app_package_name>``` with the package name of the target app (e.g., com.facebook.katana for Facebook).

---
## Notes
The script relies on the class names and method signatures of the Facebook SDK. If the SDK version changes, these might need to be updated.