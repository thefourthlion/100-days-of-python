import os

def count_python_files():
    current_folder = os.getcwd()
    python_files = [file for file in os.listdir(current_folder) if file.endswith(".py")]
    count = len(python_files)
    print(f"You've written {count} Python scripts!")

count_python_files()

