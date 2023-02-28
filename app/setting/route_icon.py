from flask import request, flash
import os
import random
import string

# función para renombrar imágenes con una cadena aleatoria
def rename_image(archivos, ruta):
    for archivo in archivos:
        longitud_cadena = 10 # longitud de la cadena aleatoria
        cadena_aleatoria = ''.join(random.choices(string.ascii_letters, k=longitud_cadena)) # genera una cadena aleatoria
        old_name = os.path.join(ruta, archivo) # obtiene el nombre del archivo original
        new_name = os.path.join(ruta, f'{cadena_aleatoria}.png') # crea un nuevo nombre de archivo con la cadena aleatoria
        os.rename(old_name, new_name) # renombra el archivo

def file(png):
    ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', 'icon') # establece la carpeta de destino para el archivo cargado
    os.makedirs(ruta, exist_ok=True) # crea la carpeta si no existe
    archivos = os.listdir(ruta) # obtiene una lista de todos los archivos en la carpeta
    cantidad = len(archivos) # obtiene el número de archivos en la carpeta
    if cantidad > 0: # si ya hay archivos en la carpeta
        rename_image(archivos, ruta) # renombra los archivos con cadenas aleatorias
    png.save(os.path.join(ruta, 'code.png')) # guarda el archivo cargado en la carpeta de destino con el nombre especificado
    
# función principal para manejar las carga de archivo 
def function():
    icon_png = request.files.get('icon_png') # obtiene el archivo cargado para el campo de formulario "icon_png"
    if not icon_png: # si hay un archivo cargado para el campo "portada"
        flash('se necesita cargar un archivo para subirlo a la plataforma') #mandamos un mensaje de que el formulario esta vacio y salimos sin guardar cambios
        return
    file(icon_png) # guarda el archivo en la carpeta "icon" con el nombre "code.png"
    flash('icono actualizado')# muestra un mensaje para confirmar que el archivo se ha guardado correctamente