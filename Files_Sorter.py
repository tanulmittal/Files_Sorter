import os
import shutil

def organize_files(directory):
    for filename in os.listdir(directory):
        # Get file extension
        extension = os.path.splitext(filename)[1]

        # Create a new directory for the extension
        new_directory = os.path.join(directory, extension)

        # Create new directory if it does not exist
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)

        # Get the current file path
        old_file_path = os.path.join(directory, filename)

        # Get the new file path
        new_file_path = os.path.join(new_directory, filename)

        # Move the file to the new directory
        shutil.move(old_file_path, new_file_path)

    # Print "Files Sorted" after the code execution
    print("Files Sorted")

# Call the function with the directory you want to organize
organize_files("/path/Your_Messy_Folder")