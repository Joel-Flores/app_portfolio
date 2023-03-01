from flask import request, flash
from app.db import get_db
from werkzeug.security import generate_password_hash

def register_user():
    db, c = get_db()
        
    username = request.form['username']
    password = request.form['password']
    error = None
    
    query = 'SELECT id FROM user WHERE nick_name = %s'
    values = [username]
    c.execute(query, values)
    
    if not username:
        error = 'usuario es requerido'
    elif not password:
        error = 'password es requerido'
    elif c.fetchone() is not None:
        error = f'usuario {username} se encuentra registrado'

    if error is None:
        query = 'INSERT INTO user (nick_name, password, register_active) VALUES (%s,%s, %s)'
        password = generate_password_hash(password)
        values = [username,password,1]
        c.execute(query, values)
        db.commit() 
        
    return error