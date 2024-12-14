import tkinter as tk
from tkinter import filedialog
from metadata import get_metadata, extract_coordinates
from steg import extract_steg_message
import textwrap 

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
            formatted_message = f"-----BEGIN PGP PUBLIC KEY BLOCK-----\n"
            formatted_message += textwrap.fill(message.strip(), width=64)
            formatted_message += f"\n-----END PGP PUBLIC KEY BLOCK-----"
            pgp_text.delete(1.0, tk.END)  # Очистка текстового виджета
            pgp_text.insert(tk.END, formatted_message)  # Вставка форматированного текста
            pgp_text.tag_add("center", 1.0, "end")  # Применение тега для центрирования
        else:
            pgp_text.delete(1.0, tk.END)
            pgp_text.insert(tk.END, "No hidden message found.")
            pgp_text.tag_add("center", 1.0, "end")  # Центрирование

root = tk.Tk()
root.title("Image Inspector")
root.geometry("500x400")

open_button = tk.Button(root, text="Open Image (GPS)", command=open_file)
open_button.pack(pady=10)

pgp_button = tk.Button(root, text="Extract PGP Key", command=extract_pgp_key)
pgp_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Создание текстового виджета с прокруткой
frame = tk.Frame(root)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

pgp_text = tk.Text(frame, wrap=tk.WORD, padx=10, pady=10)
pgp_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, command=pgp_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

pgp_text.config(yscrollcommand=scrollbar.set)

# Добавление тега для выравнивания текста по центру
pgp_text.tag_configure("center", justify="center")

root.mainloop()
