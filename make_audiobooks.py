import os
import openai
import subprocess
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
OPENAI_API_KEY = " "

# Path to your text file
text_file_path = './book.txt'  # Replace with your file path

# Function to split text into chunks
def split_text(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

# Read the text from the file
with open(text_file_path, 'r') as file:
    your_text = file.read()

# Split the text into chunks of 4096 characters
chunks = split_text(your_text, 4096)

# Create OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Extract filename without extension
filename_without_extension = Path(text_file_path).stem

# List to hold the names of the generated MP3 files
mp3_files = []

# Process each chunk
for i, chunk in enumerate(chunks):
    mp3_filename = f'{filename_without_extension}-{i+1}.mp3'
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",  # other voices: 'echo', 'fable', 'onyx', 'nova', 'shimmer'
        input=chunk
    )
    response.stream_to_file(mp3_filename)
    mp3_files.append(mp3_filename)

# Concatenate MP3 files using FFmpeg
output_filename = f'{filename_without_extension}-combined.mp3'
concat_command = f"ffmpeg -y -i \"concat:{'|'.join(mp3_files)}\" -acodec copy {output_filename}"
subprocess.run(concat_command, shell=True)

# Optional: Remove individual MP3 files after concatenation
for file in mp3_files:
    os.remove(file)
