import os
import shutil

audible_folder = r"F:\media\Audio Books\audible-download"
mp3_folder = r"F:\media\Audio Books\mp3"
output_file = r"F:\media\Audio Books\audible-not-converted\unconverted_files.txt"
output_folder = r"F:\media\Audio Books\audible-not-converted"

# Get a list of .aax files in the audible folder
audible_files = [f for f in os.listdir(audible_folder) if f.endswith(".aax")]

# Get a list of .mp3 files in the mp3 folder
mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith(".mp3")]

# Compare the filenames and copy the unconverted .aax files to the output folder
unconverted_files = []
for audible_file in audible_files:
    mp3_file = os.path.splitext(audible_file)[0] + ".mp3"
    if mp3_file not in mp3_files:
        source_path = os.path.join(audible_folder, audible_file)
        destination_path = os.path.join(output_folder, audible_file)
        shutil.copyfile(source_path, destination_path)
        unconverted_files.append(audible_file)

# Save the filenames of the unconverted files to a text document
with open(os.path.join(output_folder, output_file), 'w') as file:
    file.write(f"Number of unconverted files: {len(unconverted_files)}\n\n")
    file.write("Unconverted Files:\n")
    for filename in unconverted_files:
        file.write(filename + '\n')

# Print the number of unconverted files
print("Number of unconverted files:", len(unconverted_files))