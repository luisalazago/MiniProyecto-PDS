--Tabla Usuario

CREATE TABLE usuario(
	idUsuario numeric(10) primary key not null,
	nombre char(50) not null,
	contrasena char(20) not null,
	tipo bool not null); 
	
--Tabla Producto

CREATE TABLE producto(
	codigoBarra numeric(15) primary key,
	nombre char(20) not null,
	precio numeric(8) not null,
	cantidad numeric(5) not null,
	capacidad numeric(5) not null);

--Tabla Venta
CREATE TABLE venta(
	idVenta numeric(10),
	idProducto numeric(15),
	cantidad numeric(4),
	primary key(idVenta, idProducto),
		foreign key(idProducto)
			references producto(codigoBarra));
	
--Tabla registros de ventas
CREATE TABLE registroVenta(
	idRegistro numeric(10) primary key not null,
	usuario numeric(11) not null,
	idCliente_venta numeric(11),
	infoVenta char(200),
	fecha date not null,
	foreign key(usuario)
		references usuario(idUsuario));

--Tabla categoria productos
CREATE TABLE categoria(
	codigo numeric(8) primary key,
	nombre char(20) not null);