import qrcode
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import os

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter text or URL")
        return

    qr_color = color_var.get()

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=qr_color, back_color="white").convert("RGB")

    # Add logo
    if logo_path.get():
        logo = Image.open(logo_path.get())
        logo_size = img.size[0] // 4
        logo = logo.resize((logo_size, logo_size))
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        img.paste(logo, pos)

    # Save file
    file_name = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")])
    if file_name:
        img.save(file_name)
        os.startfile(file_name)
        messagebox.showinfo("Success", "QR Code generated successfully!")

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_var.set(color)

def choose_logo():
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if path:
        logo_path.set(path)

# GUI Window
window = tk.Tk()
window.title("Advanced QR Code Generator")
window.geometry("420x350")

tk.Label(window, text="Enter Text or URL", font=("Arial", 12)).pack(pady=5)
entry = tk.Entry(window, width=40)
entry.pack(pady=5)

tk.Button(window, text="Choose QR Color", command=choose_color).pack(pady=5)
color_var = tk.StringVar(value="black")

tk.Button(window, text="Add Logo (Optional)", command=choose_logo).pack(pady=5)
logo_path = tk.StringVar()

tk.Button(window, text="Generate QR Code", command=generate_qr,
          font=("Arial", 12, "bold"), bg="green", fg="white").pack(pady=15)

window.mainloop()
