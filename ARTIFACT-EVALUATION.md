# Artifact Appendix

Paper title: Privacy Settings of Third-Party Libraries in Android Apps: A Study of Facebook SDKs

Artifacts HotCRP Id: 11

Requested Badge: **Available**

## Description
The submitted artifacts support the study presented in the paper _Privacy Settings in Third-Party Libraries in Android Applications: A Study on Facebook SDKs_. These include two tools that enable the methods and analyses described in the paper:

1. **Frida-based Privacy Analysis Tool**: This tool serves to analyze Facebook SDKs integrated into Android apps, tracking privacy-related settings at runtime. It detects settings modifications made through the app Manifest, code, or the Meta Developers Platform, aligning with the paper’s dynamic analysis methodology.
2. **Maven Library Crawler and LibScout Profile Generator**: This tool suite automates the retrieval of libraries from Maven repositories, generates XML metadata, and creates LibScout profiles, enabling library identification and privacy-related analysis as detailed in the paper.

These tools directly reflect the core contributions of the paper, fostering reproducibility of results and further exploration of SDK-related privacy settings.

### Security/Privacy Issues and Ethical Concerns
The artifacts do not contain malware or sensitive data samples and are safe to use in secure environments. The tools rely on Android app analysis and Frida instrumentation but do not introduce risks that require disabling essential security mechanisms like ASLR or firewalls. No ethical concerns are associated with the artifacts.

## Basic Requirements

### Hardware Requirements
The tools do not require specialized hardware. Any modern PC with 16GB RAM and 100GB disk space is sufficient. For dynamic analysis, Android test devices are required; low-cost Android devices (e.g., Redmi 10) with a rooted configuration suffice.

### Software Requirements
- The tools should run on any operating system capable of supporting the required Python environment.
- Python (3.8 or higher) is necessary, with dependencies detailed in the requirements.txt file that can be found in the LibScout_TPL_Analysis folder.

### Estimated Time and Storage Consumption
- LibScout Profile Generation: Approximately 10 seconds per SDK version.
- Dynamic Analysis with Frida: Time depends on the desired monitoring duration:
  - Default Settings Inspection: A few seconds are sufficient.
  - Settings Changes Observation: The detection of changes made to the SDK's privacy settings may depend on the interaction performed with the application and the time spent on it. Therefore, the required time will depend on the interests of the person executing it.
- Disk Space: <1GB for storing generated profiles and APKs under analysis.

## Environment 

### Accessibility
The artifact is hosted in a public Git repository: https://github.com/DavidRodriguezTorrado/PrivacySDKSettingsAnalyzer. The specific commit ID to be evaluated for this submission is "4efcbc5".