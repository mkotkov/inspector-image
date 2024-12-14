import tkinter as tk
from tkinter import filedialog
from metadata import get_metadata, extract_coordinates
from steg import extract_steg_message

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        metadata = get_metadata(file_path)
        gps_info = metadata.get('GPSInfo', {})
        coordinates = extract_coordinates(gps_info)
        if coordinates:
            result_label.config(text=f"Coordinates: {coordinates}")
        else:
            result_label.config(text="No GPS data found.")

def extract_pgp_key():
    file_path = filedialog.askopenfilename()
    if file_path:
        message = extract_steg_message(file_path)
        if message:
            formatted_message = message.strip()
            pgp_label.config(text=formatted_message)
        else:
            pgp_label.config(text="No hidden message found.")

root = tk.Tk()
root.title("Image Inspector")
root.geometry("500x400")

open_button = tk.Button(root, text="Open Image (GPS)", command=open_file)
open_button.pack(pady=10)

pgp_button = tk.Button(root, text="Extract PGP Key", command=extract_pgp_key)
pgp_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

pgp_label = tk.Label(root, text="", justify="left", padx=10)
pgp_label.pack(pady=10)

root.mainloop()
