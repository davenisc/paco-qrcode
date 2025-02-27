# Paco QRcode Generator

<a href="https://ibb.co/cmxGd1K"><img src="https://i.ibb.co/cmxGd1K/Agent-1.png" alt="Agent-1" border="0"></a>

Una herramienta gráfica en Python para generar códigos QR personalizados. La aplicación utiliza Tkinter para la interfaz, junto con las librerías qrcode y Pillow para la generación y manipulación de imágenes. Además, incorpora un banner y un icono personalizados en la ventana.

<a href="https://ibb.co/bgW8J0k0"><img src="https://i.ibb.co/qMyP5SvS/Captura-de-pantalla-2025-02-26-193638.png" alt="Captura-de-pantalla-2025-02-26-193638" border="0"></a>

# Características
 * Generación de Códigos QR: Convierte cualquier URL en un código QR con alta corrección de errores.
 * Bordes Redondeados: Aplica una máscara a la imagen QR para obtener bordes redondeados.
 * Interfaz Gráfica: Ventana amigable construida con Tkinter que muestra un banner y permite ingresar la URL.
 * Vista Previa del QR: Muestra una vista previa del código QR generado en la misma ventana.
 * Modo Standalone Compatible: Incluye una función resource_path que permite ejecutar la aplicación tanto en modo de desarrollo como en aplicaciones congeladas (standalone) generadas con herramientas como Nuitka o PyInstaller.

# Requisitos
Python 3.8 o superior
Librerías Python:
 * qrcode
 * Pillow
 * Instalación

# Clonar el repositorio:

```bash
  git clone https://github.com/tu_usuario/Paco-QRcode-Generator.git
  cd Paco-QRcode-Generator
```

Crear y activar un entorno virtual (opcional, pero recomendado):

# En Windows:

```bash
python -m venv env
env\Scripts\activate
```
# En macOS/Linux:

```bash
python3 -m venv env
source env/bin/activate
```
# Instalar las dependencias:

```bash
pip install -r requirements.txt
```
Nota: Si no tienes un archivo requirements.txt, puedes instalar las dependencias manualmente:

```bash
pip install qrcode[pil] pillow
```
Uso
Asegúrate de tener los archivos de recursos en el mismo directorio:

# banner.png
icon.png (o icon.ico si se utiliza para el icono de la ventana)
Ejecuta el script:

```bash
python Paco_QRcode.py
```
Se abrirá una ventana donde podrás:

Ver el banner en la parte superior.
Ingresar la URL en el campo correspondiente.
Presionar el botón "Generar QR" para obtener el código QR.
Visualizar una vista previa del código QR generado.
Empaquetado en Ejecutable
Si deseas distribuir la aplicación a usuarios que no tengan Python instalado, tienes dos opciones:

# PyInstaller
Empaqueta el script en un único ejecutable (.exe) con:

```bash
pyinstaller --onefile --add-data "banner.png;." --add-data "icon.png;." Paco_QRcode.py
```
Nota: En Linux/macOS usa : en lugar de ; para separar la ruta de destino.

# Nuitka
Empaqueta la aplicación usando Nuitka con el siguiente comando:

```bash
nuitka --standalone --windows-icon-from-ico=icon.ico --include-data-file=banner.png=banner.png --include-data-file=icon.png=icon.png Paco_QRcode.py
```
La opción --standalone asegura que se incluyan todas las dependencias y la función resource_path en el código se encargará de localizar los recursos correctamente.

Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar alguna funcionalidad o agregar nuevas características, abre un issue o envía un pull request.

Licencia
Este proyecto está licenciado bajo la MIT License.

Contacto
Si tienes alguna duda o sugerencia, no dudes en contactarme:

Nombre: David Vega
https://nesshq.com
