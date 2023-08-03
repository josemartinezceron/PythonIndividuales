CREATE DATABASE nombre_base_de_datos; 
USE nombre_base_de_datos; 

CREATE TABLE OPERADORES ( 
  RUN VARCHAR(10) PRIMARY KEY, 
  nombre VARCHAR(50), 
  apellido VARCHAR(50), 
  direccion VARCHAR(100), 
  correo_electronico VARCHAR(100) 
);

CREATE TABLE USUARIOS ( 
  id_coder INT PRIMARY KEY, 
  nombre VARCHAR(50), 
  apellido VARCHAR(50), 
  correo_electronico VARCHAR(100), 
  telefono VARCHAR(20) 
);  

CREATE TABLE CAPACITACION ( 
  codigo_curso INT PRIMARY KEY, 
  nombre VARCHAR(50), 
  horario VARCHAR(50) 
); 

INSERT INTO OPERADORES (RUN, nombre, apellido, direccion, correo_electronico) VALUES  
  ('1234567890', 'Juan', 'Perez', 'Calle 123', 'juan.perez@example.com'),  
  ('0987654321', 'Maria', 'Lopez', 'Avenida 456', 'maria.lopez@example.com'),  
  ('1111111111', 'Pedro', 'González', 'Avenida Central', 'pedro.gonzalez@example.com'),  
  ('2222222222', 'Ana', 'Rodríguez', 'Calle Principal', 'ana.rodriguez@example.com'),  
  ('3333333333', 'Luis', 'Hernández', 'Avenida Norte', 'luis.hernandez@example.com'),  
  ('4444444444', 'Laura', 'Torres', 'Calle Sur', 'laura.torres@example.com'),  
  ('5555555555', 'Carlos', 'Gómez', 'Avenida Oeste', 'carlos.gomez@example.com'),  
  ('6666666666', 'Marta', 'Sánchez', 'Calle Este', 'marta.sanchez@example.com'),  
  ('7777777777', 'Javier', 'Vargas', 'Avenida 123', 'javier.vargas@example.com'),  
  ('8888888888', 'María', 'Martínez', 'Calle 456', 'maria.martinez@example.com'),
   ('9999999999', 'Ricardo', 'Gómez', 'Calle 789', 'ricardo.gomez@example.com'),   
  ('1010101010', 'Isabel', 'López', 'Avenida 987', 'isabel.lopez@example.com'),   
  ('1212121212', 'Fernando', 'Hernández', 'Calle Este', 'fernando.hernandez@example.com'); ;  

INSERT INTO CAPACITACION (codigo_curso, nombre, horario) VALUES  
  (1, 'Curso de Programación', 'Lunes 9:00 AM'),  
  (2, 'Taller de Diseño Gráfico', 'Miércoles 3:00 PM'),  
  (3, 'Curso de Marketing Digital', 'Martes 10:00 AM'),  
  (4, 'Taller de Fotografía', 'Jueves 2:00 PM'),  
  (5, 'Curso de Inglés Avanzado', 'Viernes 6:00 PM'),  
  (6, 'Taller de Cocina Saludable', 'Sábado 11:00 AM'),  
  (7, 'Curso de Finanzas Personales', 'Lunes 6:00 PM'),  
  (8, 'Taller de Yoga y Meditación', 'Miércoles 5:00 PM'),  
  (9, 'Curso de Desarrollo Personal', 'Jueves 7:00 PM'),  
  (10, 'Taller de Pintura al Óleo', 'Viernes 4:00 PM'),
  (11, 'Curso de Fotografía Digital', 'Martes 4:00 PM'),   
  (12, 'Taller de Marketing en Redes Sociales', 'Jueves 6:00 PM'),   
  (13, 'Curso de Programación Web', 'Viernes 3:00 PM'); 

ALTER TABLE CAPACITACION ADD costo DECIMAL(10,2);

UPDATE CAPACITACION SET costo = 500.00 WHERE codigo_curso = 1; 
UPDATE CAPACITACION SET costo = 400.00 WHERE codigo_curso = 2; 
UPDATE CAPACITACION SET costo = 600.00 WHERE codigo_curso = 3; 
UPDATE CAPACITACION SET costo = 450.00 WHERE codigo_curso = 4; 
UPDATE CAPACITACION SET costo = 700.00 WHERE codigo_curso = 5; 
UPDATE CAPACITACION SET costo = 350.00 WHERE codigo_curso = 6; 
UPDATE CAPACITACION SET costo = 650.00 WHERE codigo_curso = 7; 
UPDATE CAPACITACION SET costo = 550.00 WHERE codigo_curso = 8; 
UPDATE CAPACITACION SET costo = 750.00 WHERE codigo_curso = 9; 
UPDATE CAPACITACION SET costo = 650.00 WHERE codigo_curso = 10; 
UPDATE CAPACITACION SET costo = 550.00 WHERE codigo_curso = 11; 
UPDATE CAPACITACION SET costo = 450.00 WHERE codigo_curso = 12; 
UPDATE CAPACITACION SET costo = 800.00 WHERE codigo_curso = 13; 
 

ALTER TABLE OPERADORES ADD salario DECIMAL(10,2);

UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '1234567890'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '0987654321'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '1111111111'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '2222222222'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '3333333333'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '4444444444'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '5555555555'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '6666666666'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '7777777777'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '8888888888'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '9999999999'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '1010101010'; 
UPDATE OPERADORES SET salario = 50000.00 WHERE RUN = '1212121212'; 

CREATE TABLE Cursos_económicos ( 
  codigo_curso INT PRIMARY KEY, 
  nombre VARCHAR(50), 
  horario VARCHAR(50), 
  cantidad_minima_estudiantes INT DEFAULT 0, 
  aportes_publicos DECIMAL(10,2) DEFAULT 0.00
); 

INSERT INTO Cursos_económicos (codigo_curso, nombre, horario) 
SELECT codigo_curso, nombre, horario
FROM CAPACITACION 
WHERE costo < (SELECT AVG(costo) FROM CAPACITACION);

INSERT INTO CAPACITACION (codigo_curso, nombre, horario, costo) VALUES    
  (14, 'Curso de Programación Avanzada', 'Lunes 11:00 AM', 850.00),    
  (15, 'Taller de Diseño UX/UI', 'Miércoles 4:00 PM', 650.00),    
  (16, 'Curso de SEO y SEM', 'Martes 9:00 AM', 700.00),    
  (17, 'Taller de Fotografía de Retrato', 'Jueves 3:00 PM', 500.00),    
  (18, 'Curso de Francés Intermedio', 'Viernes 7:00 PM', 600.00);   
 
INSERT INTO OPERADORES (RUN, nombre, apellido, direccion, correo_electronico, salario) VALUES    
  ('1313131313', 'Sofía', 'González', 'Calle 789', 'sofia.gonzalez@example.com', 55000.00),    
  ('1414141414', 'Roberto', 'López', 'Avenida 987', 'roberto.lopez@example.com', 60000.00),     
  ('1515151515', 'Lucía', 'Hernández', 'Calle Este', 'lucia.hernandez@example.com', 65000.00);  