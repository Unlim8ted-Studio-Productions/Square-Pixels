import os
import zipfile
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import win32com.client
import winshell

# Specify the game archive path
archive_path = "Square Pixel.zip"

# Specify the icon path
icon_path = "icons_scalable.ico"


def create_start_menu_shortcut(extract_path, shortcut_name):
    shortcut_folder = os.path.join(winshell.programs(), "Your Game Folder")
    if not os.path.exists(shortcut_folder):
        os.makedirs(shortcut_folder)

    shortcut_path = os.path.join(shortcut_folder, f"{shortcut_name}.lnk")
    target_path = os.path.join(
        extract_path, "game.exe"
    )  # Change 'game.exe' to the actual game executable

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = extract_path
    shortcut.IconLocation = icon_path  # Set the icon location
    shortcut.save()

    return shortcut_path


def create_desktop_shortcut(extract_path, shortcut_name):
    shortcut_path = os.path.join(
        os.path.expanduser("~"), "Desktop", f"{shortcut_name}.lnk"
    )
    target_path = os.path.join(
        extract_path, "game.exe"
    )  # Change 'game.exe' to the actual game executable

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = target_path
    shortcut.WorkingDirectory = extract_path
    shortcut.IconLocation = icon_path  # Set the icon location
    shortcut.save()

    return shortcut_path


def unzip_game_archive(extract_path, progress_bar, details_label):
    try:
        with zipfile.ZipFile(archive_path, "r") as zip_ref:
            total_files = len(zip_ref.infolist())
            extracted_files = 0

            for file_info in zip_ref.infolist():
                zip_ref.extract(file_info, extract_path)
                extracted_files += 1
                progress = int((extracted_files / total_files) * 100)
                progress_bar["value"] = progress
                progress_bar.update()
                details_label.config(text=f"Extracted {extracted_files}/{total_files} files")

        return True
    except Exception as e:
        return False


def open_folder_dialog():
    install_location = filedialog.askdirectory(title="Select Install Location")
    if install_location:
        install_location_entry.delete(0, tk.END)
        install_location_entry.insert(0, install_location)


def install_game():
    install_location = install_location_entry.get()
    shortcut_name = shortcut_name_entry.get()

    if not os.path.exists(install_location):
        os.makedirs(install_location)

    progress_bar["value"] = 0
    progress_bar.update()

    details_label.config(text="Starting installation...")

    if unzip_game_archive(install_location, progress_bar, details_label):
        progress_bar["value"] = 100

        if shortcut_name:
            create_start_menu_shortcut(
                install_location, shortcut_name
            )  # Create Start menu shortcut
            result_label.config(
                text="Game installed successfully.\nStart menu shortcut created."
            )
        else:
            result_label.config(text="Game installed successfully.")
    else:
        result_label.config(text="Extraction failed. Please check the archive path.")


# Create a GUI window
root = tk.Tk()
root.title("Game Installer")
root.geometry("400x350")  # Larger window size

# Create and arrange widgets
install_location_label = tk.Label(root, text="Install Location:")
install_location_label.pack()
install_location_entry = tk.Entry(root)
install_location_entry.pack()

browse_button = tk.Button(root, text="Browse", command=open_folder_dialog)
browse_button.pack()

shortcut_name_label = tk.Label(root, text="Shortcut Name:")
shortcut_name_label.pack()
shortcut_name_entry = tk.Entry(root)
shortcut_name_entry.pack()

install_button = tk.Button(root, text="Install Game", command=install_game)
install_button.pack()

progress_bar = ttk.Progressbar(root, mode="determinate")
progress_bar.pack()

details_label = tk.Label(root, text="", pady=10)  # Label for installation details
details_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
