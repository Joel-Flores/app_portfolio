from flask import request, flash
from app.db import get_db
import os

def file(svgFile, file_name):
    # Función auxiliar para guardar el archivo de imagen SVG en la carpeta de iconos de cursos.
    ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', 'icon_course')
    # Se crea la ruta de la carpeta donde se guardarán los archivos de imagen SVG.
    os.makedirs(ruta, exist_ok=True)
    # Se crea la carpeta si no existe.
    file_name = f'{file_name}.svg'
    # Se agrega la extensión .svg al nombre del archivo.
    svgFile.save(os.path.join(ruta, file_name))
    # Se guarda el archivo SVG en la ruta especificada.
    return file_name

def function():
    # Esta función permite agregar un nuevo curso a la base de datos.
    db, c = get_db()
    # Obtiene una conexión y un cursor a la base de datos.
    titulo = request.form['titulo']
    # Obtiene el título del curso desde el formulario enviado por el usuario.
    url = request.form['url']
    # Obtiene la URL del curso desde el formulario enviado por el usuario.
    svgFile = request.files.get('svgFile')
    # Obtiene el archivo SVG de imagen del formulario enviado por el usuario.
    file_route = file(svgFile, titulo)
    # Llama a la función auxiliar para guardar el archivo SVG en la carpeta de iconos de cursos.
    file_route = f'images/icon_course/{file_route}'
    # Crea la ruta donde se almacenará el archivo SVG dentro de la carpeta de iconos de cursos.
    sql = 'INSERT INTO cursos(nombre, icono_ruta, url) VALUES(%s, %s, %s)'
    # Define la consulta SQL para insertar un nuevo curso en la tabla de cursos.
    values = [titulo, file_route, url]
    # Define los valores a insertar en la consulta SQL.
    c.execute(sql, values)
    # Ejecuta la consulta SQL con los valores especificados.
    db.commit()
    # Guarda los cambios en la base de datos.
    flash('curso agregado')
    # Muestra un mensaje flash al usuario indicando que el curso ha sido agregado con éxito.
