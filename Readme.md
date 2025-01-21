# Privacy Settings Analysis and Maven Library Crawling Tools

This repository details the technical contributions of the paper _Privacy Settings in Third-Party Libraries in Android Applications: A Study on Facebook SDKs_, accepted for publication at the Privacy Enhancing Technologies Symposium (PETs) 2025. It contains two distinct projects that contribute to the study of privacy settings in Android third-party libraries, particularly Facebook SDKs.

The two primary tools in this repository are:

1. **Frida-based Privacy Analysis Tool**: A tool designed to dynamically analyze privacy-related settings of Facebook SDKs integrated into Android applications.
2. **Maven Library Crawler and LibScout Profile Generator**: A suite of tools to crawl and download libraries from Maven repositories, generate XML metadata, and create LibScout profiles for these libraries.

For further technical details, please refer to the individual project directories.

---

## Repository Structure

The repository is structured into two main directories:

### 1. **Frida_TPL_Analysis**
This directory contains the artifacts for analyzing privacy-related settings in third-party libraries using the **Frida** instrumentation toolkit.

#### Features:
- Detects the integration of Facebook Core and Audience Network SDKs in Android apps.
- Logs SDK privacy-related settings and tracks any runtime modifications.
- Outputs results in a structured JSON-like format.

Refer to the [Frida_TPL_Analysis Readme](Frida_TPL_Analysis/Readme.md) for setup instructions, usage details, and prerequisites.

---

### 2. **LibScout_TPL_Analysis**
This directory includes tools to facilitate:
- Crawling and downloading libraries from Maven repositories.
- Generating XML metadata for libraries.
- Creating LibScout profiles for detailed library analysis.

#### Workflow:
The tools follow a structured pipeline:
1. **Library Crawling**: Crawl Maven repositories to download specified libraries (via `crawl_libraries.py`).
2. **Setup Dependencies**: Set up the necessary tools and LibScout environment (`setup.py`).
3. **Run Checks**: Validate the setup to ensure the correct configuration (`run_checks.py`).
4. **Generate XML Metadata**: Create XML metadata for the crawled libraries (`xml_files_generator.py`).
5. **Profile Generation**: Generate LibScout profiles for the libraries (`profile_generator.py`).

Refer to the [LibScout_TPL_Analysis Readme](LibScout_TPL_Analysis/Readme.md) for detailed instructions.

---

## Citation

If you use this repository in your research, please cite the following accepted PETs paper:

**Title**: *Privacy Settings in Third-Party Libraries in Android Applications: A Study on Facebook SDKs*  
**Authors**: David Rodriguez, Joseph A. Calandrino, Jose M. Del Alamo, Norman Sadeh  
**Status**: Accepted for publication at the Privacy Enhancing Technologies Symposium (PETs) 2025.

Once the paper is published, the official link and DOI will be added to this repository.

---

## License

This repository is licensed under the **PolyForm Noncommercial License 1.0.0**. This license applies to all files and content in this repository.

### Permissions:
- **Use**: You are free to use this work for non-commercial purposes.
- **Share**: You may copy and redistribute the material in any medium or format.
- **Adapt**: You may remix, transform, or build upon the material for non-commercial purposes.

### Conditions:
- **Attribution**: You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- **NonCommercial**: You may not use the material for commercial purposes.

### License Details:
For more information, visit the [PolyForm Noncommercial License Website](https://polyformproject.org/licenses/noncommercial/1.0.0/).

---

For additional questions or support, feel free to reach out via the issue tracker in this repository.
