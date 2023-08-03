CREATE TABLE usuarios (
  id_usuario INT PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  contraseña VARCHAR(50),
  zona_horaria VARCHAR(50) DEFAULT 'UTC-3',
  género VARCHAR(10),
  teléfono_contacto VARCHAR(20)
);

CREATE TABLE ingresos (
  id_ingreso INT PRIMARY KEY,
  id_usuario INT,
  fecha_ingreso DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

CREATE TABLE visitas (
  id_visita INT PRIMARY KEY,
  id_usuario INT,
  cantidad_visitas INT,
  FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario)
);

DROP TABLE visitas; 
