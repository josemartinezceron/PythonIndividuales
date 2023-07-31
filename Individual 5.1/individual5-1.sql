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
  ('8888888888', 'María', 'Martínez', 'Calle 456', 'maria.martinez@example.com'); 
INSERT INTO USUARIOS (id_coder, nombre, apellido, correo_electronico, telefono) VALUES 
  (1, 'Pedro', 'Gonzalez', 'pedro.gonzalez@example.com', '1234567890'), 
  (2, 'Ana', 'Rodriguez', 'ana.rodriguez@example.com', '0987654321'), 
  (3, 'Luis', 'Hernandez', 'luis.hernandez@example.com', '9876543210'), 
  (4, 'Maria', 'Lopez', 'maria.lopez@example.com', '0123456789'), 
  (5, 'Juan', 'Perez', 'juan.perez@example.com', '3456789012'), 
  (6, 'Laura', 'Torres', 'laura.torres@example.com', '5678901234'), 
  (7, 'Carlos', 'Gomez', 'carlos.gomez@example.com', '7890123456'), 
  (8, 'Marta', 'Sanchez', 'marta.sanchez@example.com', '9012345678'), 
  (9, 'Javier', 'Vargas', 'javier.vargas@example.com', '2345678901'), 
  (10, 'Maria', 'Martinez', 'maria.martinez@example.com', '4567890123');  
 
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
  (10, 'Taller de Pintura al Óleo', 'Viernes 4:00 PM'); 