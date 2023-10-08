import os
import hashlib

def hash_file(file_path, block_size=65536):
    """Calculate the hash (SHA-256) of a file."""
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

def find_duplicate_files(folder):
    """Find duplicate files in the specified folder."""
    file_hash_dict = {}
    duplicates = []

    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = hash_file(file_path)
            if file_hash in file_hash_dict:
                duplicates.append((file_path, file_hash_dict[file_hash]))
            else:
                file_hash_dict[file_hash] = file_path

    return duplicates

def remove_duplicates(duplicates):
    """Remove duplicate files, keeping one copy of each."""
    for duplicate_pair in duplicates:
        duplicate_file, _ = duplicate_pair
        print(f"Deleting duplicate: {duplicate_file}")
        os.remove(duplicate_file)


if __name__ == "__main__":
    current_folder = os.getcwd()
    print(f"Searching for duplicates in the current folder: {current_folder}")
    
    duplicates = find_duplicate_files(current_folder)
    
    if duplicates:
        print("Duplicate files found:")
        for duplicate_pair in duplicates:
            print(f"{duplicate_pair[0]} (Duplicate of {duplicate_pair[1]})")

        confirmation = input("Do you want to delete the duplicates? (yes/no): ")
        if confirmation.lower() == "yes":
            remove_duplicates(duplicates)
            print("Duplicates removed.")
        else:
            print("No duplicates were removed.")
    else:
        print("No duplicate files found.")
