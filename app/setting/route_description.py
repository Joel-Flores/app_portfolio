from flask import request, flash
from app.db import get_db

def function():
    # Obtiene una conexión y un cursor a la base de datos a través de la función get_db().
    db, c = get_db()

    # Define una consulta SQL con un marcador de posición para el valor de la profesión a insertar.
    sql = 'INSERT INTO descripcion(titulo, descripcion, opcional_descripcion) VALUES (%s, %s, %s)'

    # Obtiene los valores ingresados por el usuario para el título, la descripción principal y la descripción opcional.
    titulo = request.form['titulo']
    principal = request.form['principal']
    opcional = request.form['Opcional']
    values = [titulo, principal, opcional]

    # Verifica que el campo de título, descripción principal y opcional no esté vacío.
    if not titulo and not principal and not opcional:
        flash('Los campos no pueden estar vacíos')
        return
        
    # Ejecuta la consulta SQL con los valores ingresados por el usuario como argumentos.
    c.execute(sql, values)
        
    # Guarda los cambios en la base de datos.
    db.commit()
        
    # Muestra un mensaje flash para el usuario indicando que la Descripcion fue modificada y se ha agregado con éxito.
    flash('Descripcion modificada')