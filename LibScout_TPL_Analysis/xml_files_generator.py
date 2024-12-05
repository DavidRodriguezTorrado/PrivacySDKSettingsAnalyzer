import os
import pandas as pd


def parse_categ(category):
    if category == 'Development':
        return 'Utilities'
    elif category == 'Ad Networks':
        return 'Advertising'
    elif category == 'Social':
        return 'SocialMedia'
    return category


def parse_xml(name, category, version):
    return """<?xml version="1.0"?>
<library>
	<!-- library name, e.g. "Google Admob" -->
	<name>{}</name>

	<!-- category, any of "Advertising", "Analytics", "Android", "Cloud", "SocialMedia", "Utilities" -->
	<category>{}</category>

	<!-- optional: version string, e.g. "4.0.4" -->
	<version>{}</version>

	<!-- optional: date (format: dd.MM.yyyy  example: 21.05.2017) -->
	<!-- <releasedate></releasedate> -->

	<!-- optional: comment -->
	<!-- <comment></comment> -->
</library>""".format(name, category, version)


if __name__ == '__main__':

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
        raise FileNotFoundError("File with SDKs crawled to generate their XMLs not found in Crawling_Results folder. "
                                "Please execute the crawl_libraries.py script first.")

    df = pd.read_csv(SDKs_To_Process).dropna(subset='sdk_names_found')
    df['Library_categ_LibScout'] = df['Library_category'].apply(lambda x: parse_categ(x))
    count = 0
    for name, category, versions in zip(df['Library'], df['Library_categ_LibScout'], df['sdk_versions_downloaded']):
        if isinstance(versions, float):
            continue
        versions = versions.split(', ')
        for version in versions:
            xml_content = parse_xml(name, category, version)
            open('./assets/{}-{}.xml'.format(name.replace(' ', '_'), version), 'w').write(xml_content)
            count += 1
    print('{} xml files created!'.format(count))
