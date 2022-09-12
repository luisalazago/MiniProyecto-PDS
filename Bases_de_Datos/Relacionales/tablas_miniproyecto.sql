--Tabla Usuario
CREATE TABLE usuario(
	idUsuario numeric(10) primary key,
	nombre char(50) not null,
	contrasena char(20) not null,
	tipo bool not null); 

--Tabla categoria productos
CREATE TABLE categoria(
	codigo numeric(8) primary key,
	nombre char(20) not null);

--Tabla Producto
CREATE TABLE producto(
	codigoBarra numeric(15) primary key,
	nombre char(20) not null,
	precio numeric(8) not null,
	cantidad numeric(5) not null,
	capacidad numeric(5) not null,
	tipo numeric(8) references categoria(codigo) not null);

--Tabla registros de ventas
CREATE TABLE registroVenta(
	idRegistro bigint primary key GENERATED ALWAYS AS IDENTITY,
	usuario numeric(11) not null,
	idCliente_venta numeric(11),
	infoVenta char(200),
	fecha date not null,
	foreign key(usuario) references usuario(idUsuario));

--Tabla Venta
CREATE TABLE venta(
	idVenta bigint references registroVenta(idRegistro),
	idProducto numeric(15) references producto(codigoBarra),
	cantidad numeric(5),
	primary key(idVenta, idProducto));
	
--ALTER TABLE registroVenta 
--ALTER COLUMN idRegistro ADD GENERATED ALWAYS AS IDENTITY;

--DROP TABLE venta;
--DROP TABLE registroventa;
--DROP TABLE producto;
--DROP TABLE usuario;
--DROP TABLE categoria;
