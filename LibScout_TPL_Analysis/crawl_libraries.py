import pandas as pd
import os
import logging
import argparse
from helping_methods import tp_library_to_mvn_path, load_website, get_tp_library_versions, get_tp_library_jar

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def analyze_sdk(package_name, base_mvn_path):
    """Analyze a single SDK from Maven Repository."""
    logger.info(f'Analyzing SDK: {package_name}')

    sdk_versions_url = os.path.join(base_mvn_path, tp_library_to_mvn_path(package_name))
    sdk_versions_soup = load_website(sdk_versions_url)

    if not sdk_versions_soup:
        logger.warning(f'Could not retrieve data for SDK: {package_name}')
        return '', 'Not found', '', ''

    sdk_versions = get_tp_library_versions(sdk_versions_soup)
    sdk_versions_found = ', '.join(sdk_versions)
    sdk_versions_downloaded = []
    sdk_files = []
    sdk_name_found = ''

    for sdk_version in sdk_versions:
        jars_url = os.path.join(sdk_versions_url, sdk_version)
        res, sdk, file = get_tp_library_jar(soup=load_website(jars_url), url=jars_url)
        if res:
            sdk_versions_downloaded.append(sdk_version)
            sdk_files.append(file)
        sdk_name_found = sdk

    return (
        sdk_name_found,
        sdk_versions_found,
        ', '.join(sdk_versions_downloaded),
        ', '.join(sdk_files) if sdk_files else ''
    )


def process_sdk_list(input_csv, output_csv, base_mvn_path):
    """Process a list of SDKs from a CSV file."""
    df = pd.read_csv(input_csv).head(5)
    logger.info(f'Loaded {len(df)} SDKs from {input_csv}')

    results = {
        'sdk_names_found': [],
        'sdk_versions_found': [],
        'sdk_versions_downloaded': [],
        'sdk_files_stored': []
    }

    for pkg_name in df['SDK_name']:
        if isinstance(pkg_name, float):  # Skip invalid rows
            logger.warning('Skipping invalid SDK name.')
            for key in results:
                results[key].append('')
            continue

        sdk_name, versions_found, versions_downloaded, files_stored = analyze_sdk(pkg_name, base_mvn_path)
        results['sdk_names_found'].append(sdk_name)
        results['sdk_versions_found'].append(versions_found)
        results['sdk_versions_downloaded'].append(versions_downloaded)
        results['sdk_files_stored'].append(files_stored)

    for key, value in results.items():
        df[key] = value

    df.to_csv(output_csv, index=False)
    logger.info(f'Results saved to {output_csv}')


def main():
    parser = argparse.ArgumentParser(description="Analyze Android SDKs from Maven repository.")
    parser.add_argument('--input', required=True, help="Path to input CSV file containing SDK names.")
    parser.add_argument('--output', required=True, help="Path to output CSV file for results.")
    parser.add_argument('--base-url', default="https://repo1.maven.org/maven2/", help="Base URL for Maven repository.")

    args = parser.parse_args()

    process_sdk_list(args.input, args.output, args.base_url)


if __name__ == '__main__':
    main()
