import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess


def check_version(filepath):
    """Retrieve the file version of an executable."""
    try:
        if not filepath or not os.path.isfile(filepath):
            raise FileNotFoundError("Invalid file selected.")
        
        file_info = subprocess.run(["wmic", "datafile", "where", f"name='{filepath.replace('\\', '\\\\')}'", "get", "Version"], 
                                    capture_output=True, text=True)
        output = file_info.stdout.strip().split("\n")
        if len(output) > 1 and output[1].strip():
            return output[1].strip()
        else:
            return "No version information found."
    except Exception as e:
        return f"Error: {str(e)}"


def browse_file():
    """Open a file dialog to select an executable file."""
    filepath = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
    if filepath:
        entry_filepath.delete(0, tk.END)
        entry_filepath.insert(0, filepath)


def show_version():
    """Display the version information for the selected executable."""
    filepath = entry_filepath.get()
    version = check_version(filepath)
    messagebox.showinfo("Version Info", f"File: {filepath}\nVersion: {version}")


# Create the GUI
app = tk.Tk()
app.title("Version Verifier")
app.geometry("500x200")

# Filepath entry
lbl_filepath = tk.Label(app, text="Executable File Path:")
lbl_filepath.pack(pady=10)
entry_filepath = tk.Entry(app, width=50)
entry_filepath.pack(pady=5)
btn_browse = tk.Button(app, text="Browse", command=browse_file)
btn_browse.pack(pady=5)

# Check version button
btn_check_version = tk.Button(app, text="Check Version", command=show_version)
btn_check_version.pack(pady=20)

# Run the GUI
app.mainloop()
