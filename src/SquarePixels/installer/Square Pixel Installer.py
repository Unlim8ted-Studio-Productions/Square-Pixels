import os
import zipfile
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import win32com.client
import winshell
import requests
import tempfile
import sys
from modified_requests import urlretrieve

# uc?id=&download=1&confirm=t
# Specify the URLs for the game archive and icon on Google Drive (very specific url minipulations do not change for regular share url)
archive_url = "https://drive.google.com/uc?id=1GYmDlRhRTMIV-pBAQx_8C7zHzomfFljR&download=1&confirm=t&uuid=0dc20ea1-74e0-4bbb-a868-1bc282f97370&at=AB6BwCBxVB0vHdXu5I9RsO4Tp8cy:1696975557238"
icon_path = urlretrieve(
    "https://drive.google.com/uc?id=14lGwOvuIN4sAWe560LDiJ8LdmQZeEuEl&download=1&confirm=t"
)
# if hasattr(sys, "_MEIPASS"):
#    # Running as a bundled executable
#    icon_path[0] = os.path.join(sys._MEIPASS, "icons scalable.ico")
# else:
#    # Running as a regular script
#    icon_path[0] = "icons scalable.ico"

cleaned_temp = False


def create_start_menu_shortcut(extract_path, shortcut_name):
    extract_path += "Square Pixel\\"
    shortcut_folder = os.path.join(winshell.programs(), "Unlim8ted Studio Productions")
    if not os.path.exists(shortcut_folder):
        os.makedirs(shortcut_folder)

    shortcut_path = os.path.join(shortcut_folder, f"{shortcut_name}.lnk")
    target_path = os.path.join(
        extract_path, "Square Pixel.exe"
    )  # Change 'game.exe' to the actual game executable

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = extract_path
    shortcut.IconLocation = (
        extract_path
        + "\\Recources\PE EXE file compile recources\icons scalable.ico"  # Set the icon location
    )
    shortcut.save()

    return shortcut_path


def create_desktop_shortcut(extract_path, shortcut_name):
    extract_path += "Square Pixel\\"
    shortcut_path = os.path.join(
        os.path.expanduser("~"), "Desktop", f"{shortcut_name}.lnk"
    )
    target_path = os.path.join(
        extract_path, "Square Pixel.exe"
    )  # Change 'game.exe' to the actual game executable

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = extract_path
    shortcut.IconLocation = (
        extract_path
        + "\\Recources\PE EXE file compile recources\icons scalable.ico"  # Set the icon location
    )
    shortcut.save()

    return shortcut_path


def unzip_game_archive(archive_pathh, extract_path, progress_bar, details_label):
    try:
        with zipfile.ZipFile(archive_pathh, "r") as zip_ref:
            total_files = len(zip_ref.infolist())
            extracted_files = 0

            for file_info in zip_ref.infolist():
                zip_ref.extract(file_info, extract_path)
                extracted_files += 1
                progress = int((extracted_files / total_files) * 100)
                progress_bar["value"] = progress
                progress_bar.update()
                details_label.config(
                    text=f"Extracted {extracted_files}/{total_files} files"
                )

        return True
    except Exception as e:
        return False


def open_folder_dialog():
    install_location = filedialog.askdirectory(title="Select Install Location")
    if install_location:
        install_location_entry.delete(0, tk.END)
        install_location_entry.insert(0, install_location)


def download_file_to_temp(url):
    try:
        temp_dir = tempfile.gettempdir()
        response = requests.get(url)
        temp_file_path = os.path.join(temp_dir, os.path.basename(url))

        with open(temp_file_path, "wb") as file:
            file.write(response.content)
        return temp_file_path
    except Exception as e:
        return None


def cleanup_temp_files(temp_files):
    for temp_file in temp_files:
        try:
            os.remove(temp_file)
        except Exception as e:
            print(f"Failed to delete temp file: {temp_file}")


def install_game():
    global archive_path, cleaned_temp
    # archive_path = download_file_to_temp(archive_path)
    install_location = install_location_entry.get()
    # shortcut_name = shortcut_name_entry.get()
    temp_files = []  # List to hold temporary file paths

    if not os.path.exists(install_location):
        os.makedirs(install_location)

    progress_bar["value"] = 0
    progress_bar.update()

    details_label.config(text="Starting installation...")

    if archive_path:
        temp_files.extend([archive_path, icon_path])  # Add temporary files to the list

        if unzip_game_archive(
            archive_path, install_location, progress_bar, details_label
        ):
            progress_bar["value"] = 100

            create_start_menu_shortcut(
                install_location, "Square Pixel"
            )  # Create Start menu shortcut
            if not create_desktop_shortcut_var:
                result_label.config(
                    text="Game installed successfully.\nStart menu shortcut created."
                )
            else:
                create_desktop_shortcut(install_location, "Square Pixel")
                result_label.config(
                    text="Game installed successfully.\nStart menu shortcut created.\n Desktop Shortcut Created"
                )
        else:
            result_label.config(
                text="Extraction failed. Please check the archive path."
            )
    else:
        result_label.config(text="Download failed. Please check the URLs.")

    # Clean up the temporary files
    try:
        os.remove(icon_path)
        os.remove(archive_path)
        cleaned_temp = True
    except IOError as e:
        print(e)
    # cleanup_temp_files(temp_files)


# Create a GUI window
root = tk.Tk()
root.title("Square Pixel Installer")
root.geometry("400x350")  # Larger window size
# Set the window icon
os.rename(icon_path[0], icon_path[0] + ".ico")
icon_path = icon_path[0] + ".ico"
root.iconbitmap(icon_path)
archive_path = urlretrieve(
    archive_url,
    tpcobject=root,
)
os.rename(archive_path[0], archive_path[0] + ".zip")
archive_path = archive_path[0] + ".zip"
# Create and arrange widgets
install_location_label = tk.Label(root, text="Install Location:")
install_location_label.pack()
install_location_entry = tk.Entry(root)
install_location_entry.pack()

browse_button = tk.Button(root, text="Browse", command=open_folder_dialog)
browse_button.pack()

# shortcut_name_label = tk.Label(root, text="Shortcut Name:")
# shortcut_name_label.pack()
# shortcut_name_entry = tk.Entry(root)
# shortcut_name_entry.pack()

# if not a:
#    shortcut_name_entry.setvar("Square Pixel")
#    a = True

# Checkbox to create desktop shortcut
create_desktop_shortcut_var = tk.BooleanVar()
create_desktop_shortcut_var.set(True)  # Default: Create desktop shortcut

create_desktop_shortcut_checkbox = tk.Checkbutton(
    root, text="Create Desktop Shortcut", variable=create_desktop_shortcut_var
)
create_desktop_shortcut_checkbox.pack()

install_button = tk.Button(root, text="Install Game", command=install_game)
install_button.pack()

progress_bar = ttk.Progressbar(root, mode="determinate")
progress_bar.pack()

details_label = tk.Label(root, text="", pady=10)  # Label for installation details
details_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()

if not cleaned_temp:
    try:
        os.remove(icon_path)
        os.remove(archive_path)
    except IOError as e:
        print(e)
