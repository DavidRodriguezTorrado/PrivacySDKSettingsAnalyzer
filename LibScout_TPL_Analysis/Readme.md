# Maven Library Crawler and LibScout Profile Generator

This project provides a complete workflow for crawling and downloading libraries from Maven repositories, performing checks, and automatically generating LibScout profiles. The workflow uses a series of scripts to achieve this goal in a structured manner.

---

## Prerequisites

1. **Python 3.8+**:
   - Ensure Python 3.8 or higher is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Python Dependencies**:
   - Install the required Python libraries by running the following command:
     ```bash
     pip install -r requirements.txt
     ```
   - This will ensure all necessary libraries, including `pandas`, are installed.

3. **Java Runtime**:
   - This project has been tested with the following Java version:
     ```plaintext
     java version "19.0.1" 2022-10-18
     Java(TM) SE Runtime Environment (build 19.0.1+10-21)
     Java HotSpot(TM) 64-Bit Server VM (build 19.0.1+10-21, mixed mode, sharing)
     ```
   - It is recommended to use a similar or compatible version. You can download Java from [Oracle](https://www.oracle.com/java/technologies/javase-downloads.html) or install via your system's package manager:
     - For Ubuntu:
       ```bash
       sudo apt install default-jre
       ```
     - For macOS (via Homebrew):
       ```bash
       brew install openjdk
       ```

4. **Maven Repository Access**:
   - Ensure your machine has internet access to crawl libraries from Maven repositories.

---

## Workflow

### 1. Crawl Libraries (`crawl_libraries.py`)

The script `crawl_libraries.py` crawls the Maven repository to download libraries based on the `ExampleSDKs.csv` file.

#### Input:
- The `ExampleSDKs.csv` file provides the list of SDKs and their metadata.

#### Usage:
The script requires three arguments:
1. **`--input`**: Path to the input CSV file containing SDK names.
2. **`--output`**: Path to the output CSV file for results.
3. **`--base-url`**: (Optional) Base URL for the Maven repository. Defaults to `https://repo1.maven.org/maven2/`.

#### Steps:
1. Run the script:
    ```bash
    python crawl_libraries.py --input Source_SDKs/ExampleSDKs.csv --output Crawling_Results/CrawlingResults.csv
    ```
2. The output is saved in the `Crawling_Results/CrawlingResults.csv` file, which contains details about the crawled libraries.

Note that a new folder named `TP_libraries_storage`, will be created containing the SDKs code downloaded from Maven repository.

### 2. Set Up Dependencies (`setup.py`)

The setup.py script ensures all dependencies, including the required LibScout repository, are set up properly.

Steps:
1. Run the setup script:
    ```bash
    python setup.py
    ```
2. The script performs the following:
- Clones the LibScout repository.
- Moves the necessary Python files into the LibScout directory.

### 3. Run gradlew in the LibScout folder

Run the gradlew or gradlew.bat files to ensure that the LibScout project is set up. Follow the official repository instructions.

### 4. Run Checks (`run_checks.py`)

The run_checks.py script validates the LibScout project has the necessary files to proceed.  

Steps:
Run the script:
    ```bash
    python run_checks.py    
    ```

Please, make sure that both tests are passed before proceeding.

### 5. Generate XML Files (`xml_files_generator.py`)
The xml_files_generator.py script generates XML metadata files for the libraries, which are used in creating LibScout profiles.

Steps:
Run the script:
    ```bash
    python xml_files_generator.py
    ```

Output XML files are saved in the ./assets/ directory.

### 5. Generate LibScout Profiles (profile_generator.py)
The profile_generator.py script generates LibScout profiles based on the XML files created in the previous step.

Steps:
Run the script:
    ```bash
    python profile_generator.py    
    ```

The generated profiles are stored in the LibScout directory under build/profiles.

---

## Notes
CSV File Placement:
- The ExampleSDKs.csv file should be in the Source_SDKs directory for the crawl_libraries.py script to locate it.
- The CrawlingResults.csv is generated in the Crawling_Results directory.

Error Handling:
- Ensure that the ExampleSDKs.csv file is present before running the scripts.

Customization:
- Modify the ExampleSDKs.csv file to include the libraries you want to crawl and analyze. The three columns present in that file are important.