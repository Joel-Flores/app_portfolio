instrutions = [
    "DROP TABLE IF EXISTS user;",
    "DROP TABLE IF EXISTS personal_information;",
    "DROP TABLE IF EXISTS descripcion;",
    "DROP TABLE IF EXISTS redes_sociales;",
    "DROP TABLE IF EXISTS profesiones;",
    "DROP TABLE IF EXISTS cursos;",
    "DROP TABLE IF EXISTS trabajos;",
    "DROP TABLE IF EXISTS tipo_trabajo;",
    
    """CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nick_name VARCHAR(25) UNIQUE NOT NULL,
        password VARCHAR(110) NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );
    """,
    """CREATE TABLE personal_information(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(20) NOT NULL,
        segundo_nombre VARCHAR(20) ,
        apellido VARCHAR(20) NOT NULL,
        segundo_apellido VARCHAR(20) ,
        correo VARCHAR(50) UNIQUE NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE descripcion(
        id INT PRIMARY KEY AUTO_INCREMENT,
        titulo VARCHAR(100) NOT NULL,
        descripcion TEXT NOT NULL,
        opcional_descripcion TEXT,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE redes_sociales(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre_red_social VARCHAR(20) UNIQUE NOT NULL,
        sitio_web VARCHAR(100) UNIQUE NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE profesiones(
        id INT PRIMARY KEY AUTO_INCREMENT,
        profesion VARCHAR(45) UNIQUE NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE cursos(
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(45) UNIQUE NOT NULL,
        icono_ruta VARCHAR(60) UNIQUE NOT NULL,
        url VARCHAR(100) UNIQUE NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
    );""",
    """CREATE TABLE tipo_trabajo(
        id INT PRIMARY KEY AUTO_INCREMENT,
        tipo VARCHAR(10) UNIQUE NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE
        
    );""",
    """CREATE TABLE trabajos(
        id INT PRIMARY KEY AUTO_INCREMENT,
        titutlo VARCHAR(20) UNIQUE NOT NULL,
        descripcion TEXT NOT NULL,
        url_proyecto VARCHAR(150) UNIQUE NOT NULL,
        type INT NOT NULL,
        created_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_active BIT DEFAULT TRUE,
        FOREIGN KEY (type) REFERENCES tipo_trabajo(id)
    );""",
    
    """INSERT INTO tipo_trabajo(tipo)
    VALUES ('app'), ('web'), ('card');"""
]