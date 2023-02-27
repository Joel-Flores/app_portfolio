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
        new_name = os.path.join(ruta, f'{cadena_aleatoria}.jpg') # crea un nuevo nombre de archivo con la cadena aleatoria
        os.rename(old_name, new_name) # renombra el archivo
            
# función para guardar archivos cargados en el servidor
def file(file, file_name, image):
    ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', file) # establece la carpeta de destino para el archivo cargado
    os.makedirs(ruta, exist_ok=True) # crea la carpeta si no existe
    archivos = os.listdir(ruta) # obtiene una lista de todos los archivos en la carpeta
    cantidad = len(archivos) # obtiene el número de archivos en la carpeta
    if cantidad > 0: # si ya hay archivos en la carpeta
        rename_image(archivos, ruta) # renombra los archivos con cadenas aleatorias
    image.save(os.path.join(ruta, file_name)) # guarda el archivo cargado en la carpeta de destino con el nombre especificado

# función principal para manejar las cargas de archivos
def function():
    portada = request.files.get('formImagePortada') # obtiene el archivo cargado para el campo de formulario "portada"
    perfil = request.files.get('formImagePerfil') # obtiene el archivo cargado para el campo de formulario "perfil"
    if portada: # si hay un archivo cargado para el campo "portada"
        file('home', 'home_principal.jpg', portada) # guarda el archivo en la carpeta "home" con el nombre "home_principal.jpg"
    if perfil: # si hay un archivo cargado para el campo "perfil"
        file('perfil', 'principal.jpg', perfil) # guarda el archivo en la carpeta "perfil" con el nombre "principal.jpg"
    flash('Imagen(es) actualizadas y guardadas') # muestra un mensaje para confirmar que los archivos se han guardado correctamente
