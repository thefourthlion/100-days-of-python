import os
from moviepy.editor import VideoFileClip

def is_mov_openable(mov_path):
    try:
        video_clip = VideoFileClip(mov_path)
        return True  # .mov file was successfully opened
    except Exception as e:
        print(f"Error opening .mov file '{mov_path}': {str(e)}")
        return False  # .mov file could not be opened

def delete_unopenable_movs(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.mov'):
            mov_path = os.path.join(folder_path, filename)
            if not is_mov_openable(mov_path):
                print(f"Deleting unopenable .mov file: {mov_path}")
                os.remove(mov_path)

if __name__ == "__main__":
    current_folder = os.getcwd()
    print(f"Searching for unopenable .mov files in the current folder: {current_folder}")
    
    delete_unopenable_movs(current_folder)
    print("Unopenable .mov files have been deleted.")
