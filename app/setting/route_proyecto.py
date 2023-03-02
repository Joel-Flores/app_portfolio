from flask import request, flash
from app.db import get_db
import os

def file(proyecto, img_1, img_2):
    # Crea la carpeta para guardar las imágenes del proyecto.
    ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', 'portfolio', proyecto)
    os.makedirs(ruta, exist_ok=True)
    
    # Guarda las imágenes en la carpeta del proyecto.
    file_name = f'{proyecto}_principal.jpg'
    img_1.save(os.path.join(ruta, file_name))
    file_name = f'{proyecto}_secundario.jpg'
    img_2.save(os.path.join(ruta, file_name))

def function():
    # Obtiene una conexión y un cursor a la base de datos a través de la función get_db().
    db, c = get_db()
    error = None
    # Obtiene los datos enviados por el usuario a través del formulario web.
    type_app = request.form['type_app']
    titulo = request.form['titulo']
    url = request.form['proyecto']
    url = f'https://{url}'
    descripcion = request.form['descripcion']
    portada = request.files.get('formImagePortada')
    secundario = request.files.get('formImageSecundario')
    
    # Verifica que los campos requeridos no estén vacíos.
    if type_app == 'TIPO DE PROYECTO':
        error = 'no se designo un trabajo especifico app, web, card'
        return error
    if not titulo or not url or not descripcion or not portada or not secundario:
        error ='Los campos no se llenaron correctamente'
        return error
    
    # Define la consulta SQL para insertar un nuevo proyecto en la base de datos.
    sql = 'INSERT INTO trabajos(titutlo, descripcion, url_proyecto, type) VALUES(%s, %s, %s, %s)'
    
    # Define los valores que se van a insertar en la consulta SQL.
    values = [titulo, descripcion, url, type_app]
    
    # Ejecuta la consulta SQL con los valores indicados.
    c.execute(sql, values)
    
    # Guarda los cambios en la base de datos.
    db.commit()
    
    # Guarda las imágenes del proyecto en la carpeta correspondiente.
    file(titulo, portada, secundario)
    
    # Muestra un mensaje flash para el usuario indicando que el proyecto se ha agregado con éxito.
    flash('Proyecto agregado')
