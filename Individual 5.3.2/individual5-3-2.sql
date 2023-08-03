CREATE DATABASE transacciones;

CREATE USER daniela IDENTIFIED BY 'contraseña';
   GRANT ALL PRIVILEGES ON transacciones.* TO daniela;
   
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo_electronico VARCHAR(100),
    telefono VARCHAR(15),
    genero VARCHAR(10)
);

INSERT INTO usuarios (id, nombre, apellido, correo_electronico, telefono, genero)
VALUES
    (1, 'Nombre1', 'Apellido1', 'correo1@example.com', '123456789', 'Masculino'),
    (2, 'Nombre2', 'Apellido2', 'correo2@example.com', '987654321', 'Femenino'),
    (3, 'Nombre3', 'Apellido3', 'correo3@example.com', '111111111', 'Masculino'),
    (4, 'Nombre4', 'Apellido4', 'correo4@example.com', '222222222', 'Femenino'),
    (5, 'Nombre5', 'Apellido5', 'correo5@example.com', '333333333', 'Masculino');

CREATE TABLE usuarios_especiales (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    correo_electronico VARCHAR(100),
    telefono VARCHAR(15),
    genero VARCHAR(10)
);

START TRANSACTION;

INSERT INTO usuarios_especiales (id, nombre, apellido, correo, telefono, genero)
SELECT id, nombre, apellido, correo, telefono, genero
FROM tabla1
LIMIT 3;

DELETE FROM usuarios
WHERE id IN (SELECT id FROM tabla2);

COMMIT;

START TRANSACTION;

INSERT INTO usuarios (id, nombre, apellido, correo, telefono, genero)
SELECT id, nombre, apellido, correo, telefono, genero
FROM tabla2
WHERE id = 3;

DELETE FROM usuarios_especiales
WHERE id = 3;

COMMIT;    
    