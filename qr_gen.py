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
import os

# Generate the QR code
def create_qr_code():
    user_text = text_entry.get()
    show = show_var.get()
    save = save_var.get()
    filename = filename_entry.get()

    if not user_text:
        messagebox.showwarning("Warning", "Please enter text.")
        return

    if save and not filename:
        messagebox.showwarning("Warning", "Please enter filename.")
        return

    # Crear el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(user_text)
    qr.make(fit=True)
    imagen_qr = qr.make_image(fill='black', back_color='white')

    if show:
        # show la imagen en una nueva ventana
        img = ImageTk.PhotoImage(imagen_qr)
        img_label.config(image=img)
        img_label.image = img

    if save:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, f"{filename}.png")
        imagen_qr.save(file_path)
        messagebox.showinfo("Information", f"QR code has been saved as '{filename}.png'.")

# Enable/disable the PNG filename text box
def toggle_filename_entry():
    if save_var.get():
        filename_entry.config(state='normal')
    else:
        filename_entry.config(state='disabled')

# Main window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x300")
root.configure(bg='lightblue')

# Text box for the QR string
text_label = tk.Label(root, text="Enter text for the QR code:", bg='lightblue', font=('Arial', 12))
text_label.pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

# Check box: Show QR or not
show_var = tk.BooleanVar()
show_checkbox = tk.Checkbutton(root, text="Show on screen", variable=show_var, bg='lightblue')
show_checkbox.pack()

# Check box: Save QR PNG or not
save_var = tk.BooleanVar()
save_checkbox = tk.Checkbutton(root, text="Save as PNG", variable=save_var, command=toggle_filename_entry, bg='lightblue')
save_checkbox.pack()

# PNG filename text box (disabled by default)
filename_entry = tk.Entry(root, width=30, state='disabled')
filename_entry.pack()

# Create QR code button (make the magic happen)
create_button = tk.Button(root, text="Create QR Code", command=create_qr_code, bg='blue', fg='white', font=('Arial', 12, 'bold'))
create_button.pack()

# Show QR image
img_label = tk.Label(root, bg='lightblue')
img_label.pack()

# Mainloop
root.mainloop()
