import os

# Get the current directory
folder_path = os.getcwd()

# Iterate through all files in the current directory
for filename in os.listdir(folder_path):
    # Construct the full path of the file
    file_path = os.path.join(folder_path, filename)
    
    # Check if the item is a file (not a directory)
    if os.path.isfile(file_path):
        # Extract the "File Description" from the file name if it exists
        file_description, file_extension = os.path.splitext(filename)
        if "File Description" in file_description:
            # Construct the new file name using the "File Description"
            new_filename = file_description.strip() + file_extension
            
            # Construct the full path for the new file name
            new_file_path = os.path.join(folder_path, new_filename)
            
            try:
                # Rename the file
                os.rename(file_path, new_file_path)
                print(f'Renamed "{filename}" to "{new_filename}"')
            except OSError as e:
                print(f'Error renaming "{filename}": {e}')

print('Renaming process completed.')
