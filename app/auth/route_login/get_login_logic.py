from app.db import get_db

def user_exist():
    db, c = get_db()    
    error = None
    query = 'SELECT created_in FROM user'
    c.execute(query)
    user = c.fetchall()
    
    if user == []:
        error = 'no existen usuarios, registrate'
    return error