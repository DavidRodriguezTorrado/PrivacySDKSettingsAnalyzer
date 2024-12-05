import os
import subprocess
import shutil

# Define constants
LIBSCOUT_REPO_URL = "https://github.com/reddr/LibScout.git"
LIBSCOUT_DIR = "LibScout_TPL_Analysis/LibScout"


def clone_libscout():
    """
    Clone the LibScout repository if not already present.
    """
    if os.path.exists(LIBSCOUT_DIR):
        print(f"{LIBSCOUT_DIR} directory already exists. Skipping cloning.")
    else:
        print(f"Cloning {LIBSCOUT_REPO_URL}...")
        subprocess.run(["git", "clone", LIBSCOUT_REPO_URL, LIBSCOUT_DIR], check=True)
        print(f"Cloned {LIBSCOUT_REPO_URL} into {LIBSCOUT_DIR}.")


def move_python_files():
    """
    Move the additional Python files into the LibScout directory.
    """
    files_to_move = ["LibScout_TPL_Analysis/profile_generator.py", "LibScout_TPL_Analysis/xml_files_generator.py"]
    for file in files_to_move:
        src_path = os.path.abspath(file)
        dest_path = os.path.join(LIBSCOUT_DIR, os.path.basename(file))
        if os.path.exists(src_path):
            print(f"Moving {file} to {LIBSCOUT_DIR}...")
            shutil.move(src_path, dest_path)
        else:
            print(f"File {file} not found. Please ensure it exists in the repository.")


def main():
    """
    Main setup function.
    """
    try:
        # Step 1: Clone LibScout repository
        clone_libscout()

        # Step 2: Move additional Python files
        move_python_files()

        print("Setup complete. The Python files have been moved to the LibScout directory.")
        print("IMPORTANT: Please, now execute the run_checks.py script, and make sure you pass all the checks before "
              "proceeding.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing a subprocess: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
