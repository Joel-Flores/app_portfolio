from flask import request, flash
from app.db import get_db

def function():
    # Obtiene una conexión y un cursor a la base de datos a través de la función get_db().
    db, c = get_db()
    
    # Define una consulta SQL con un marcador de posición para el valor de la profesión a insertar.
    sql =  'INSERT INTO profesiones(profesion) VALUES (%s)'
    
    # Obtiene el valor de la profesión a insertar desde el formulario enviado por el usuario.
    values = [request.form['profesion']]
    # Verifica que el campo de profesión no esté vacío.
    if not values:
        flash('El campo profesión no puede estar vacío')
        return
    
    # Ejecuta la consulta SQL con el valor de la profesión como argumento.
    c.execute(sql, values)
    
    # Guarda los cambios en la base de datos.
    db.commit()
    
    # Muestra un mensaje flash para el usuario indicando que la profesión se ha agregado con éxito.
    flash('Profesion agregada')