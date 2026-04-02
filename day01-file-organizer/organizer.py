import os
import shutil
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
}

def get_file_category(extension):
    """Returns the category of a file based on its extension."""
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def get_files(folder_path):
    """Returns a list of all files in the given folder."""
    files = []
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            files.append(item_path)
    return files

def organize_files(folder_path):
    """Moves files into categorized subfolders."""
    files = get_files(folder_path)
    summary = {}
    for file_path in files:
        extension = os.path.splitext(file_path)[1]
        category = get_file_category(extension)
        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file_path, destination_folder)
        logging.info(f"Moved {os.path.basename(file_path)} → {category}")
        summary[category] = summary.get(category, 0) + 1
    return summary

def get_file_count(folder_path):
    """Returns count of files before organizing."""
    files = get_files(folder_path)
    return len(files)

def main():
    """Main function to run the file organizer."""
    folder_path = input("Enter the folder path to organize: ")

    if not os.path.exists(folder_path):
        print("❌ Error: Folder not found!")
        return

    count = get_file_count(folder_path)
    print(f"🔍 Found {count} files to organize...")
    summary = organize_files(folder_path)
    print(f"✅ Successfully organized {count} files!")
    print("\n📊 Summary:")
    for category, total in summary.items():
        print(f"   {category}: {total} files")

if __name__ == "__main__":
    main()