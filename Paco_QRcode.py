# Instalar dependencias si es necesario:
# pip install qrcode[pil] pillow
#
# Para ejecutar el script, asegúrate de tener en el mismo directorio:
# - banner.png
# - icon.png
#
# Ejecuta el script con:
# python Paco_QRcode.py

import os
import sys
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageDraw, ImageTk
from datetime import datetime

def resource_path(relative_path: str) -> str:
    """
    Retorna la ruta absoluta del recurso, ya sea en modo script o congelado (standalone).
    """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def generar_qr(url):
    """
    Genera un código QR a partir de la URL proporcionada,
    le aplica una máscara con bordes redondeados y guarda la imagen en formato PNG.
    Retorna el nombre del archivo y la imagen generada.
    """
    # Configurar el objeto QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,    # Tamaño de cada módulo
        border=2,       # Borde blanco alrededor del QR
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Crear imagen base del QR y convertir a RGB
    img = qr.make_image(fill_color='black', back_color='white').convert('RGB')

    # Crear máscara para bordes redondeados
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    radio = img.size[0] // 10  # Radio para redondear (10% del ancho)
    draw.rounded_rectangle(
        [(0, 0), img.size],
        radius=radio,
        fill=255
    )

    # Aplicar la máscara para obtener bordes redondeados
    img.putalpha(mask)

    # Generar un nombre de archivo único utilizando la fecha y hora
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    nombre_archivo = f"qr_personalizado_{timestamp}.png"
    img.save(nombre_archivo, "PNG")

    return nombre_archivo, img

def on_generar_qr():
    """
    Función que se ejecuta al presionar el botón "Generar QR".
    Valida la URL, genera el QR, muestra un mensaje y actualiza la vista previa.
    """
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Por favor ingrese una URL")
        return
    try:
        nombre_archivo, img = generar_qr(url)
        messagebox.showinfo("Éxito", f"QR generado exitosamente: {nombre_archivo}")

        # Mostrar una vista previa del QR generado (redimensionada)
        qr_img = ImageTk.PhotoImage(img.resize((200, 200)))
        qr_label.config(image=qr_img)
        qr_label.image = qr_img  # Guardar referencia para evitar que se elimine
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar el QR: {e}")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Paco QRcode generator")

# Asignar icono a la ventana usando resource_path
try:
    icon = tk.PhotoImage(file=resource_path("icon.png"))
    root.iconphoto(False, icon)
except Exception as e:
    print("Icono no encontrado, continuando sin icono:", e)

# Marco para el banner
banner_frame = tk.Frame(root)
banner_frame.pack(pady=10)

try:
    banner_image = tk.PhotoImage(file=resource_path("banner.png"))
    banner_label = tk.Label(banner_frame, image=banner_image)
    banner_label.image = banner_image
    banner_label.pack()
except Exception as e:
    print("Banner no encontrado, se mostrará un texto por defecto:", e)
    banner_label = tk.Label(banner_frame, text="Paco QRcode generator", font=("Helvetica", 16, "bold"))
    banner_label.pack()

# Marco para la entrada de la URL y botón de generación
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

url_label = tk.Label(input_frame, text="Ingrese la URL:")
url_label.pack(side=tk.LEFT, padx=5)

url_entry = tk.Entry(input_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(root, text="Generar QR", command=on_generar_qr)
generate_button.pack(pady=10)

# Etiqueta para mostrar la vista previa del QR generado
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()

"""
Consejos:
- Asegúrate de tener los archivos 'banner.png' e 'icon.png' en el mismo directorio que este script.
- Si el banner no se carga, se mostrará un mensaje en la consola con el error.
- Puedes ejecutar el script directamente con Python:
    python Paco_QRcode.py
"""
