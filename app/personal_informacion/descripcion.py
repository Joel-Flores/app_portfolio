from app.db import get_db
def data():
    db, c = get_db()
    sql = 'SELECT * FROM descripcion ORDER BY id DESC LIMIT 1;'
    c.execute(sql)
    return c.fetchone()