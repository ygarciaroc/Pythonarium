import os
import shutil

# Define the folder you want to organize
FOLDER_TO_ORGANIZE = r"C:\Users\YourName\Downloads"  # Change this to your target folder

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".c", ".cpp", ".java", ".js", ".html", ".css"],
    "Others": []  # fallback if extension doesn't match
}

def organize_files(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isfile(file_path):
            # Get the file extension
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            # Find the matching category
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    category_folder = os.path.join(folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    print(f"Moved: {filename} -> {category}/")
                    moved = True
                    break

            # If extension not found, move to "Others"
            if not moved:
                other_folder = os.path.join(folder, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, filename))
                print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    organize_files(FOLDER_TO_ORGANIZE)
    print("✅ Files have been organized!")
