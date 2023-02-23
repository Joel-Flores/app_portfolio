from app.db import get_db

def data():
    db, c = get_db()
    sql = 'SELECT profesion FROM profesiones'
    c.execute(sql)
    return c.fetchall()