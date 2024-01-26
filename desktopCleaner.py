""" 

Desktop Organizer and Cleaner

Collect and organize files on a user's desktop and organize
them based on file type.

- List files on the desktop, sorted by file type
- Collect files into single folder
    - Sub-folder for each 
- Delete files of a certain type
- Display how much space the files take up (MB/GB)
    - Breakdown by file type

"""

import os

# List files function
def list_files_on_desktop():
    if os.name == 'posix': # Unix-based operating systems
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    elif os.name == 'nt': # Windows operating systems
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    else: 
        return "Unsupported operating system."
    
    if os.path.exists(desktop_path):
        files_on_desktop = os.listdir(desktop_path)
        return files_on_desktop
    else: 
        return "Desktop directory not found."
    
files = list_files_on_desktop()
if isinstance(files, list):
    print("Files on desktop:")
    for file in files:
        print(file)

else: 
    print(files)


# Display Desktop file sizes
    def desktop_file_sizes():
        if os.name == 'posix': # Unix-based operating systems
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        elif os.name == 'nt': # Windows operating systems
            desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        else:
            return "Unsupported operating system."
        
        if os.path.exists(desktop_path):
            files_on_desktop = os.listdir(desktop_path)
            files_with_sizes = {}
            for file_name in files_on_desktop:
                file_path = os.path.join(desktop_path, file_name)
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path)
                    files_with_sizes[file_name] = file_size
            return files_with_sizes
        else:
            return "Desktop directory not found."
        
def main():
    print("Welcome to the Desktop Organizer")
    print("Select an option:")
    print("1. List files on desktop")
    print("2. List files on desktop with sizes")

    choice = input()

    if choice == '1':
        files = list_files_on_desktop()
        if isinstance(files, list):
            print("\nFiles on desktop:")
            for file in files:
                print(file)

        else:
            print(files)
    elif choice == '2':
        files_with_sizes = desktop_file_sizes()
        if isinstance(files_with_sizes, dict):
            print("\nFiles on desktop with sizes:")
            for file_name, file_size in files_with_sizes.items():
                print(f"{file_name}: {file_size} bytes")
        else:
            print(files_with_sizes)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
    
        
            





