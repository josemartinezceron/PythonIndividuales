CREATE TABLE Usuarios (
  id_usuario INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  apellido VARCHAR(255),
  edad INT,
  correo_electronico VARCHAR(255),
  usos_app INT DEFAULT 1
);
CREATE TABLE Operarios (
  id_operario INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(255),
  apellido VARCHAR(255),
  edad INT,
  correo_electronico VARCHAR(255),
  atenciones INT DEFAULT 1
);
CREATE TABLE HistorialSoporte (
  id_soporte INT PRIMARY KEY,
  id_operario INT,
  id_usuario INT,
  fecha DATE,
  evaluacion INT,
  FOREIGN KEY (id_operario) REFERENCES Operarios(id_operario),
  FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);

-- Agregar usuarios
INSERT INTO Usuarios (id_usuario, nombre, apellido, edad, correo_electronico, usos_app)
VALUES
  (1, 'Luis', 'Hernández', 25, 'luis.hernandez@example.com', 3),
  (2, 'Ana', 'González', 30, 'ana.gonzalez@example.com', 5),
  (3, 'Carlos', 'López', 35, 'carlos.lopez@example.com', 7),
  (4, 'Sofía', 'Martínez', 28, 'sofia.martinez@example.com', 2),
  (5, 'Diego', 'Ramírez', 32, 'diego.ramirez@example.com', 4);

-- Agregar operarios
INSERT INTO Operarios (id_operario, nombre, apellido, edad, correo, atenciones)
VALUES
  (1, 'María', 'Sánchez', 27, 'maria.sanchez@example.com', 4),
  (2, 'Javier', 'Herrera', 29, 'javier.herrera@example.com',10),
  (3, 'Alejandra', 'Díaz', 33, 'alejandra.diaz@example.com',13),
  (4, 'Jorge', 'Torres', 31, 'jorge.torres@example.com', 3),
  (5, 'Laura', 'Vargas', 26, 'laura.vargas@example.com', 7);

-- Agregar operaciones de soporte
INSERT INTO HistorialSoporte (id_soporte, id_operario, id_usuario, fecha, evaluacion)
VALUES
  (1, 1, 1, '2023-05-30', 4),
  (2, 2, 2, '2023-05-29', 7),
  (3, 3, 3, '2023-05-28', 3),
  (4, 4, 4, '2023-05-27', 2),
  (5, 5, 5, '2023-05-26', 6),
  (6, 1, 1, '2023-05-25', 4),
  (7, 2, 2, '2023-05-24', 3),
  (8, 3, 3, '2023-05-23', 5),
  (9, 4, 5, '2023-05-22', 2),
  (10, 5, 3, '2023-05-21', 4);

SELECT * FROM HistorialSoporte
ORDER BY evaluacion DESC
LIMIT 3;


SELECT * FROM HistorialSoporte
ORDER BY evaluacion ASC
LIMIT 3;



SELECT id_operario, nombre, apellido, atenciones FROM Operarios
ORDER BY atenciones DESC
LIMIT 1;


SELECT id_usuario, nombre, apellido, usos_app FROM Usuarios
ORDER BY usos_app ASC
LIMIT 1;

UPDATE Usuarios
SET edad = edad + 10
WHERE id_usuario IN (1, 2, 3);

ALTER TABLE Usuarios
CHANGE correo_electronico email VARCHAR(255);

ALTER TABLE Operarios
CHANGE correo_electronico email VARCHAR(255);

SELECT *
FROM Operarios
WHERE edad > 20;

