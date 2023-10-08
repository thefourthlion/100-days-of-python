import os
import shutil

def organize_files_by_type(folder_path, exclude_extensions):
    try:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()
                
                if file_extension and file_extension not in exclude_extensions:
                    # Create a folder based on the file extension if it doesn't exist
                    target_folder = os.path.join(folder_path, file_extension[1:])
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    
                    # Move the file to the corresponding folder
                    target_path = os.path.join(target_folder, file)
                    shutil.move(file_path, target_path)
                    print(f"Moved {file} to {target_path}")
    except Exception as e:
        print(f"Error organizing files: {str(e)}")

if __name__ == "__main__":
    current_folder = os.getcwd()
    exclude_extensions = ['.py']  # Add any other extensions you want to exclude
    
    print(f"Organizing files in the current folder (excluding {', '.join(exclude_extensions)} files): {current_folder}")

    organize_files_by_type(current_folder, exclude_extensions)
    print("Files have been organized by type (excluding specified extensions).")
