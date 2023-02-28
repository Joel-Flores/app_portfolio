from flask import request, flash
from app.db import get_db

def function():
    db, c = get_db()
    
    # Obtener los datos enviados mediante el formulario.
    nombre = request.form['nombre']
    nombre_s = request.form['nombre_s']
    apellido = request.form['apellido']
    apellido_s = request.form['apellido_s']
    correo = request.form['correo']

    # Si los campos de nombre y apellido secundarios tienen valores, la consulta SQL insertará todos los campos.
    if nombre and apellido and correo:
        sql = 'INSERT INTO personal_information(nombre, segundo_nombre, apellido, segundo_apellido, correo) VALUES(%s, %s, %s, %s, %s)'
        values = [nombre, nombre_s, apellido, apellido_s, correo]
    else:
        flash('los campos requeridos están vacíos')
        return

    # Ejecutar la consulta SQL y guardar los cambios en la base de datos.
    c.execute(sql, values)
    db.commit()
    
    # Mostrar mensaje de éxito.
    flash('registros personales actualizados')
