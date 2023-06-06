import os
import subprocess

def extract_7z_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".7z"):
                file_path = os.path.join(root, file)
                output_folder = os.path.splitext(file_path)[0]
                subprocess.run(["7z", "x", "-o" + output_folder, file_path])

# Specify the root folder containing the subfolders with 7z files
root_folder = "/path/to/root/folder"

extract_7z_files(root_folder)

