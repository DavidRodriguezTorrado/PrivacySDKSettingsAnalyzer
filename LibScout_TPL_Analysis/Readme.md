# Maven Library Crawler and LibScout Profile Generator

This project provides a complete workflow for crawling and downloading libraries from Maven repositories, performing checks, and automatically generating LibScout profiles. The workflow uses a series of scripts to achieve this goal in a structured manner.

---

## Recommended Workflow: Using Docker

The easiest and most reliable way to use this repository is via the provided Docker container. This approach ensures all dependencies are pre-installed and configured correctly.

### Docker Image

The Docker image for this project is publicly available at:

**Image Name**: `davidrodrigueztorrado/libscout-env`

### Container Setup:

1. Pull the Docker image:
   ```bash
   docker pull davidrodrigueztorrado/libscout-env:3.0
   ```
   (_Only non ARM64 architectures_) Please note that the image's architecture is ARM64. If you want to run it on different architecture, please run the following command:
    ```bash
    docker run --rm --privileged tonistiigi/binfmt --install all
    ```
2. Run the Docker container:
   ```bash
   docker run -it --workdir /LibScout_TPL_Analysis davidrodrigueztorrado/libscout-env:3.0
   ```
3. Run the Python virtual environment:
   ```bash
   source venv/bin/activate
   ```

---

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

```
python crawl_libraries.py --input Source_SDKs/ExampleSDKs.csv --output Crawling_Results/CrawlingResults.csv
```

3. The output is saved in the `Crawling_Results/CrawlingResults.csv` file, which contains details about the crawled libraries.

Note that a new folder named `TP_libraries_storage`, will be created containing the SDKs code downloaded from the Maven repository.

---

### 2. Generate XML Files (`xml_files_generator.py`)
The xml_files_generator.py script generates XML metadata files for the libraries, which are used in creating LibScout profiles.

Steps:

Navigate to the LibScout folder:
```bash
  cd LibScout
```

Run the script:

```
python xml_files_generator.py
```

Output XML files are saved in the ./assets/ directory.

---

### 3. Generate LibScout Profiles (`profile_generator.py`)
The profile_generator.py script generates LibScout profiles based on the XML files created in the previous step.

Steps:

Run the script:

```
python profile_generator.py
```

The generated profiles are stored in the LibScout directory under `LibScout/profiles/Utilities`.

## Alternative Workflow: Local Deployment

If Docker is not an option, you can deploy the project locally. However, you must ensure that the correct software versions are installed, particularly for Java, as this is a strict requirement from LibScout gradle versions.

### Prerequisites

1. **Python 3.8+**:
   - Ensure Python 3.8 or higher is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Python Dependencies**:
   - Install the required Python libraries by running the following command:
     ```
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
       ```
       sudo apt install default-jre
       ```
     - For macOS (via Homebrew):
       ```
       brew install openjdk
       ```

4. **Maven Repository Access**:
   - Ensure your machine has internet access to crawl libraries from Maven repositories.

---

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

```
python crawl_libraries.py --input Source_SDKs/ExampleSDKs.csv --output Crawling_Results/CrawlingResults.csv
```

3. The output is saved in the `Crawling_Results/CrawlingResults.csv` file, which contains details about the crawled libraries.

Note that a new folder named `TP_libraries_storage`, will be created containing the SDKs code downloaded from the Maven repository.

### 2. Set Up Dependencies (`setup.py`)

The setup.py script ensures all dependencies, including the required LibScout repository, are set up properly.

Steps:
1. Run the setup script:

```
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

```
python run_checks.py    
```

Please, make sure that both tests are passed before proceeding.

### 5. Generate XML Files (`xml_files_generator.py`)
The xml_files_generator.py script generates XML metadata files for the libraries, which are used in creating LibScout profiles.

Steps:

Run the script:

```
python xml_files_generator.py
```

Output XML files are saved in the ./assets/ directory.

### 5. Generate LibScout Profiles (`profile_generator.py`)
The profile_generator.py script generates LibScout profiles based on the XML files created in the previous step.

Steps:

Run the script:

```
python profile_generator.py
```

The generated profiles are stored in the LibScout directory under LibScout/profiles/Utilities.

---

## Notes
CSV File Placement:
- The ExampleSDKs.csv file should be in the Source_SDKs directory for the crawl_libraries.py script to locate it.
- The CrawlingResults.csv is generated in the Crawling_Results directory.

Error Handling:
- Ensure that the ExampleSDKs.csv file is present before running the scripts.

Customization:
- Modify the ExampleSDKs.csv file to include the libraries you want to crawl and analyze. The three columns present in that file are important.