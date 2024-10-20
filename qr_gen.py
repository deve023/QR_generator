# Std Python libraries
import subprocess
import sys

# Verify and install required packages
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = ["tkinter", "qrcode"]

for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        install_package(package)

# Required libraries
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

# Generate the QR code
def create_qr_code():
    texto_usuario = text_entry.get()
    mostrar = mostrar_var.get()
    guardar = guardar_var.get()
    nombre_archivo = filename_entry.get()

    if not texto_usuario:
        messagebox.showwarning("Warning", "Please enter text.")
        return

    if guardar and not nombre_archivo:
        messagebox.showwarning("Warning", "Please enter filename.")
        return

    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto_usuario)
    qr.make(fit=True)
    imagen_qr = qr.make_image(fill='black', back_color='white')

    if mostrar:
        # Mostrar la imagen en una nueva ventana
        img = ImageTk.PhotoImage(imagen_qr)
        img_label.config(image=img)
        img_label.image = img

    if guardar:
        imagen_qr.save(f"{nombre_archivo}.png")
        messagebox.showinfo("Information", f"QR code has been saved as '{nombre_archivo}.png'.")

# Enable/disable the PNG filename text box
def toggle_filename_entry():
    if guardar_var.get():
        filename_entry.config(state='normal')
    else:
        filename_entry.config(state='disabled')

# Main window
root = tk.Tk()
root.title("QR Code Generator")

# Text box for the QR string
text_label = tk.Label(root, text="Enter text for the QR code:")
text_label.pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Check box: Show QR or not
mostrar_var = tk.BooleanVar()
mostrar_checkbox = tk.Checkbutton(root, text="Show on screen", variable=mostrar_var)
mostrar_checkbox.pack()

# Check box: Save QR PNG or not
guardar_var = tk.BooleanVar()
guardar_checkbox = tk.Checkbutton(root, text="Save as PNG", variable=guardar_var, command=toggle_filename_entry)
guardar_checkbox.pack()

# PNG filename text box (disabled by default)
filename_entry = tk.Entry(root, width=30, state='disabled')
filename_entry.pack()

# Create QR code button (make the magic happen)
create_button = tk.Button(root, text="Create QR Code", command=create_qr_code)
create_button.pack()

# Show QR image
img_label = tk.Label(root)
img_label.pack()

# Mainloop
root.mainloop()
