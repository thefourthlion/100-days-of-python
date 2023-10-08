from PIL import Image

# Get the current directory
folder_path = os.getcwd()

# Iterate through all files in the current directory
for filename in os.listdir(folder_path):
    # Construct the full path of the file
    file_path = os.path.join(folder_path, filename)
    
    # Check if the item is a file (not a directory)
    if os.path.isfile(file_path):
        try:
            # Open the image file and extract the title (description)
            with Image.open(file_path) as img:
                file_description = img.get("title", "")
                if file_description:
                    # Construct the new file name using the description
                    new_filename = file_description + os.path.splitext(filename)[1]
                    
                    # Construct the full path for the new file name
                    new_file_path = os.path.join(folder_path, new_filename)
                    
                    # Rename the file
                    os.rename(file_path, new_file_path)
                    print(f'Renamed "{filename}" to "{new_filename}"')
        except OSError as e:
            print(f'Error renaming "{filename}": {e}')

print('Renaming process completed.')
