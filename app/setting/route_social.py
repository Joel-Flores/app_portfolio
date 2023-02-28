from flask import request, flash
from app.db import get_db

def function():
    # Obtiene una conexión y un cursor a la base de datos a través de la función get_db().
    db, c = get_db()
    
    # Obtiene el valor del titulo y url desde el formulario enviado por el usuario.
    titulo = request.form['titulo']
    url = request.form['url']
    url = f'http://{url}'
    
    # Verifica que los campos no estén vacíos.
    if not titulo and not url:
        flash('debe llenar todos los campos')
        return
    
    # Define una consulta SQL con un marcador de posición para el valor de la nombre_red_social, sitio_web a insertar.
    sql = 'INSERT INTO redes_sociales(nombre_red_social, sitio_web) VALUES (%s, %s)'
    
    # Agregamos los valoes que envio al usuario, guardarlos de una lista llamada values.
    values = [titulo, url]
    
    # Ejecuta la consulta SQL con el valor de values como argumento.
    c.execute(sql, values)
    
    # Guarda los cambios en la base de datos.   
    db.commit()
    
    # Muestra un mensaje flash para el usuario indicando que se ha agregado una nueva red social con éxito.
    flash('Red social agregada')