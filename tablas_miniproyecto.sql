--Tabla Usuario

CREATE TABLE usuario(
	idUsuario serial primary key not null unique ,
	nombre char(50) not null,
	contrasena char(20) not null,
	tipo bool not null); 
	
--Tabla Producto

CREATE TABLE producto(
	codigoBarra numeric(15) primary key unique,
	nombre char(20) not null,
	precio numeric(8) not null,
	cantidad numeric(5) not null,
	capacidad numeric(5) not null);