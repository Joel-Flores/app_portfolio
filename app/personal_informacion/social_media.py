from app.db import get_db

def data():
    db, c = get_db()
    sql = 'SELECT nombre_red_social  AS name, sitio_web AS link FROM redes_sociales'
    c.execute(sql)
    return c.fetchall()