from app.db import get_db

def data():
    db, c = get_db()
    sql = 'SELECT nombre, icono_ruta, url FROM cursos'
    c.execute(sql)
    return c.fetchall()