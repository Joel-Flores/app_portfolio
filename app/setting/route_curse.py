from flask import request, flash
from app.db import get_db
import os

def file(svgFile, file_name):
    ruta = os.path.join(os.getcwd(), 'app', 'static', 'images', 'icon_course')
    os.makedirs(ruta, exist_ok=True)
    file_name = f'{file_name}.svg'
    svgFile.save(os.path.join(ruta, file_name))
    return file_name

def function():
    db, c = get_db()
    titulo = request.form['titulo']
    url = request.form['url']
    svgFile = request.files.get('svgFile')
    file_route = file(svgFile, titulo)
    file_route = f'images/icon_course/{file_route}'
    sql = 'INSERT INTO cursos(nombre, icono_ruta, url) VALUES(%s, %s, %s)'
    values = [titulo, file_route, url]
    c.execute(sql, values)
    db.commit()
    flash('curso agregado')