import os


def verify_files():
    """
    Verifies that essential files for LibScout are present.
    """
    libscout_jar_path = "LibScout/build/libs/LibScout.jar"
    android_jar_path = "LibScout/androidplatforms/android-30/android.jar"

    libscout_jar_exists = os.path.exists(libscout_jar_path)
    android_jar_exists = os.path.exists(android_jar_path)

    print("\nTo ensure that you can proceed:")
    if libscout_jar_exists:
        print(f'✔ "{libscout_jar_path}" is present.')
    else:
        print(f'✘ "{libscout_jar_path}" is missing. Please ensure you have built LibScout using "./gradlew build".')

    if android_jar_exists:
        print(f'✔ "{android_jar_path}" is present.')
    else:
        print(f'✘ "{android_jar_path}" is missing.')
        print("You can download the required `android.jar` from:")
        print("   - Android Studio: Install the Android 11 SDK via the SDK Manager.")
        print("   - GitHub: https://github.com/Sable/android-platforms/tree/master/android-30")
        print("Place the `android.jar` file in the `LibScout/androidplatforms/android-30/` directory.")

    if not libscout_jar_exists or not android_jar_exists:
        print("\nPlease resolve the missing files before proceeding.")
    else:
        print("\nAll required files are present. You can proceed!")


# Example usage
if __name__ == "__main__":
    verify_files()
