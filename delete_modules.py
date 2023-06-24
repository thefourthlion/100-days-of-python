import os
import shutil

def delete_node_modules(directory):
    for root, dirs, files in os.walk(directory):
        if "node_modules" in dirs:
            node_modules_dir = os.path.join(root, "node_modules")
            print("Deleting:", node_modules_dir)
            shutil.rmtree(node_modules_dir)

# Specify the directory to start the search from
target_directory = "Z:\programming"

# Call the function to delete "node_modules" folders recursively
delete_node_modules(target_directory)

