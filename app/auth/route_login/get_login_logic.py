from app.db import get_db

def user_exist():
    db, c = get_db()    
    error = None
    ''' c.execute('DROP TABLE IF EXISTS user;')
    query = """
    CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nick_name VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );
    """
    c.execute(query) '''
    query = 'SELECT created_in FROM user'
    c.execute(query)
    user = c.fetchall()
    
    if user == []:
        error = 'no existen usuarios, registrate'
    return error