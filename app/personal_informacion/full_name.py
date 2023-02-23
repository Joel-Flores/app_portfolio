from app.db import get_db

def data():
    db, c = get_db()
    sql = 'SELECT * FROM personal_information'
    c.execute(sql)
    return c.fetchone()