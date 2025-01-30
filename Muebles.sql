CREATE DATABASE IF NOT EXISTS TIENDA;
USE TIENDA;
CREATE TABLE muebles(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion VARCHAR(255) NOT NULL,
    precio DECIMAL(9,2) NOT NULL,
    precioIVA DECIMAL(9,2) NOT NULL,
	foto LONGTEXT
);
CREATE TABLE usuarios(
	usuario VARCHAR(100) NOT NULL PRIMARY KEY,
    clave VARCHAR(255) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    fechaUltimoAcceso DATE
);

INSERT INTO `usuarios` (`usuario`, `clave`, `perfil`, `fechaUltimoAcceso`) VALUES ('root', '1234', 'admin', NOW());
INSERT INTO `muebles` (`nombre`, `descripcion`, `precio`, `precioIVA`, `foto`) VALUES ('mesa', 'mesa', 10, 12.1, NULL);