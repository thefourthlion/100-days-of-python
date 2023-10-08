import os

def delete_shortcut_files(folder_path):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".lnk"):
                    shortcut_path = os.path.join(root, file)
                    os.remove(shortcut_path)
                    print(f"Deleted shortcut: {shortcut_path}")
    except Exception as e:
        print(f"Error deleting shortcut files: {str(e)}")

if __name__ == "__main__":
    current_folder = os.getcwd()
    print(f"Searching for shortcut files in the current folder: {current_folder}")

    delete_shortcut_files(current_folder)
    print("Shortcut files have been deleted.")
