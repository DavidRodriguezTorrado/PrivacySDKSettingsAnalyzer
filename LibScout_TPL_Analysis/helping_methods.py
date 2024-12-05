import shutil
import zipfile
import os
import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)


def get_sdk_name_from_url(url):
    """
    Based on the Maven repository url of Third party library, we want to get the sdk name.
    :param url: URL of the Third party library's Maven repository; (For example:
    https://repo1.maven.org/maven2/com/adcolony/sdk/4.4.1/)
    :return: The sdk name separated by '_'. This is used to identify the sdk name given by us from the original .jar
    file name
    """
    url_parsed = url[url.find('maven2/') + 7:]
    if url_parsed[-1] == '/':
        url_parsed = url_parsed[:url_parsed.rfind('/')]
    url_parsed = url_parsed[:url_parsed.rfind('/')].replace('/', '_')
    return url_parsed


def process_aar_file(aar_file_path, output_directory=None):
    # Check if the .aar file exists
    if not os.path.exists(aar_file_path):
        logging.warning("The .aar file does not exist.")
        return False

    # Step 1: Rename .aar to .zip
    base_name = os.path.splitext(os.path.basename(aar_file_path))[0]
    zip_file_path = os.path.join(os.path.dirname(aar_file_path), f"{base_name}.zip")
    os.rename(aar_file_path, zip_file_path)

    # Step 2: Unzip the file
    extract_folder = os.path.join(os.path.dirname(zip_file_path), base_name)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

    # Step 3: Search for a .jar file
    jar_found = False
    for root, dirs, files in os.walk(extract_folder):
        for file in files:
            if file.endswith('.jar'):
                jar_found = True
                jar_file_path = os.path.join(root, file)
                # Step 4: Rename and move the .jar file
                new_jar_name = f"{base_name}.jar"
                if output_directory is not None:
                    new_jar_path = os.path.join(output_directory, new_jar_name)
                else:
                    new_jar_path = os.path.join(os.path.dirname(aar_file_path), new_jar_name)
                shutil.move(jar_file_path, new_jar_path)
                break
        if jar_found:
            break

    # Step 5: Delete the original .zip file and the extracted folder
    os.remove(zip_file_path)
    shutil.rmtree(extract_folder)

    return jar_found


def tp_library_to_mvn_path(TP_library):
    """
    We are making sure that the dots "." are not replaced with "/" if they appear after a ":". Otherwise that could be
    leading to errors; for example in org.jetbrains.kotlin.android:org.jetbrains.kotlin.android.gradle.plugin
    :param TP_library: The package name; for example 'com.adcolony:sdk'
    :return: The structure used in MVN repository; for example 'https://repo1.maven.org/maven2/com/adcolony/sdk/'
    """
    parts = TP_library.split(':', 1)  # Split at the first colon
    parts[0] = parts[0].replace('.', '/')  # Replace dots with slashes in the first part

    return '/'.join(parts)  # Reassemble the string with a slash replacing the colon


def load_website(url, s=None):
    """
    :param url: The url we want to parse to BeautifulSoup
    :param s: Session object to allow faster page load
    :return: BeautifulSoup object
    """
    if s is None:
        s = requests.session()
    response = s.get(url)
    if response.status_code != 200:
        return None
    try:
        soup = BeautifulSoup(response.content, 'lxml')
    except:
        return None
    return soup


def get_tp_library_versions(soup):
    """
    :param soup: BeautifulSoup object
    :return: A list containing the TP libraries versions available in Maven Repository for a specific TP library
    """
    folders = []
    for link in soup.find_all('a'):
        href = link.get('href')
        # Check if the href attribute exists and if it's a folder
        if href and href.endswith('/') and 'maven' not in href and '../' not in href:
            folders.append(href.replace('/', ''))
    return folders


def get_tp_library_jar(soup, url, save_directory="./TP_libraries_storage", uncompress_aar=False):
    """
    This method downloads the .jar file for a specific version of a Third party library available in the Maven
    repository. There are two ways considered here: 1) the .jar file is directly available in the repository of that
    version or 2) there is a .aar file available.
    If the 2) choice happens, the .aar file is converted to .zip, then it is decompressed and the .jar in it is
    extracted (if there is). This .jar file is saved with the version name.

    :param soup: BeautifulSoup object of the website where the TP library's version code is available
    :param url: URL of the website corresponding to the previous BeautifulSoup object. This is needed to get the whole
    url of the .jar file downloadable.
    :param save_directory: Local folder where we want to store the .jar files.
    :param uncompress_aar: Boolean to decide if we want to extract the .jar file from the .aar one or not.
    :return: 3 outputs:
        1) True or False depending on whether we managed to find and download the .jar file or not.
        2) The SDK name.
        3) The name of the .jar file stored.
        (e.g., we store com_appodeal_ads_sdk_sdk-3.0.1.0.jar, where com.appodeal.ads:sdk is the sdk and
        sdk-3.0.1.0.jar is the .jar file name)
    """

    # Ensure save_directory exists
    os.makedirs(save_directory, exist_ok=True)

    sdk_name = get_sdk_name_from_url(url)  # Extract the SDK name from the Maven URL

    # Attempt to locate the .jar file directly in the Maven repository
    file_link = None
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('.jar') and 'source' not in href.lower() and 'javadoc' not in href.lower():
            file_link = href
            break

    # If no .jar file is found, check for .aar files
    if file_link is None:
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.endswith('.aar'):
                file_link = href
                break

    # If file_link is found, proceed with the download process
    if file_link:
        try:
            file_url = os.path.join(url, file_link)
            response = requests.get(file_url, stream=True)
            response.raise_for_status()

            filename = file_url.split('/')[-1]
            filepath = os.path.join(save_directory, f"{sdk_name}_{filename}")

            # Check if the file is already downloaded
            if os.path.exists(filepath) or os.path.exists(
                os.path.join(save_directory, filepath[filepath.rfind('/') + 1:filepath.rfind('.')] + '.jar')
            ):
                logger.debug(f"File already downloaded: {sdk_name}_{filename}")
                return True, sdk_name, f"{sdk_name}_{filename}"

            # Download the file
            with open(filepath, 'wb') as file:
                for chunk in response.iter_content(chunk_size=128):
                    file.write(chunk)

            # Handle .aar files if found
            if file_link.endswith('.aar'):
                if uncompress_aar:
                    output = process_aar_file(filepath)
                    if not output:
                        logger.warning(f"No .jar file found in .aar compressed file: {filename}")
                        return False, '', ''
                    else:
                        logger.info(f"File downloaded from .aar file: {sdk_name}_{filename}")
                        return True, sdk_name, f"{sdk_name}_{filename}"
                else:
                    logger.info(f"File (.aar) downloaded: {sdk_name}_{filename}")
                    return True, sdk_name, f"{sdk_name}_{filename}"

            # Handle .jar files
            elif file_link.endswith('.jar'):
                logger.info(f"File downloaded: {sdk_name}_{filename}")
                return True, sdk_name, f"{sdk_name}_{filename}"

            # Unmanaged situation
            else:
                logger.error(f"Unmanaged situation: File name: {file_link}")
                return False, '', ''
        except Exception as e:
            logger.error(f"Failed to download file: {e}")
            return False, '', ''
    else:
        logger.warning("No .jar nor .aar files found.")
        return False, '', ''
