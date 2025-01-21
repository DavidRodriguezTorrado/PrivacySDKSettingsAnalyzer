import subprocess
import pandas as pd
import os

def run_libscout(jar_path, android_sdk_path, library_xml_path, library_file_path):
    """
    Executes the LibScout command with the provided parameters.

    Parameters:
    - jar_path: The path to the LibScout.jar file.
    - android_sdk_path: The path to the Android SDK jar.
    - library_xml_path: The path to the library XML file.
    - library_file_path: The path to the library file.
    """
    command = [
        "java",
        "-jar",
        jar_path,
        "-o",
        "profile",
        "-a",
        android_sdk_path,
        "-x",
        library_xml_path,
        library_file_path
    ]

    # Execute the command
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Command executed successfully:")
        print(result.stdout)
        return 0
    except subprocess.CalledProcessError as e:
        print("Error occurred while executing the command:")
        print(e.stderr)
        return 1


# Example usage
if __name__ == "__main__":

    CRAWLING_RESULTS_FOLDER = '../Crawling_Results'
    RESULTS_FILE = 'Crawling_Results/CrawlingResults.csv'
    SDKs_To_Process = ''

    if os.path.exists(CRAWLING_RESULTS_FOLDER):
        if os.path.exists(os.path.join(CRAWLING_RESULTS_FOLDER, RESULTS_FILE)):
            SDKs_To_Process = os.path.join(CRAWLING_RESULTS_FOLDER, RESULTS_FILE)
        files = os.listdir(CRAWLING_RESULTS_FOLDER)
        for file in files:
            if '.csv' in file:
                SDKs_To_Process = '{}/{}'.format(CRAWLING_RESULTS_FOLDER, file)

    if SDKs_To_Process == '':
        raise FileNotFoundError("File with SDKs crawled to generate their Profiles not found in Crawling_Results folder. "
                                "Please execute the crawl_libraries.py and the xml_files_generator.py first.")

    count = 0
    df = pd.read_csv(SDKs_To_Process).dropna(subset='sdk_names_found')

    jar_path = "build/libs/LibScout.jar"
    android_sdk_path = "androidplatforms/android-30/android.jar"
    i = 0
    for libName, sdk_files in zip(df['Library'], df['sdk_files_stored']):
        print('Analyzing library {} out of {}'.format(i, len(df)))
        i += 1
        if not isinstance(sdk_files, str):
            continue

        sdk_list = sdk_files.split(', ')  # We split the list of different sdk versions corresponding to a specific sdk
        for sdk in sdk_list:
            # For each sdk, we are going to generate the profile...
            sdk_version = sdk[sdk.rfind('-')+1:sdk.rfind('.')]
            library_xml_path = "assets/{}-{}.xml".format(libName.replace(' ', '_'), sdk_version)
            library_file_path = "../TP_libraries_storage/{}".format(sdk)

            res = run_libscout(jar_path, android_sdk_path, library_xml_path, library_file_path)
            if res == 0:
                count = count + 1
    print('\n-----------------------------------------------\nTOTAL Profiles generated: ', count)
