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


                                    





