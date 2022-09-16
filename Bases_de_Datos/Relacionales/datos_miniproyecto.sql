--Datos

--Registros usuario
insert into usuario(idusuario, nombre, contrasena, tipo)
values (1000000000, 'Maria', 1234, TRUE);

insert into usuario(idusuario, nombre, contrasena, tipo)
values (1000000001, 'Luis', 1234, TRUE);

insert into usuario(idusuario, nombre, contrasena, tipo)
values (1000000002, 'Guido', 1234, TRUE);

insert into usuario(idusuario, nombre, contrasena, tipo)
values (1000000003, 'Josefa', 1234, FALSE);

insert into usuario(idusuario, nombre, contrasena, tipo)
values (1000000004, 'Carlos', 1234, FALSE);


--Registros categoria
insert into categoria(codigo, nombre)
values (1000, 'Bebidas');

insert into categoria(codigo, nombre)
values (2000, 'Carnes');

insert into categoria(codigo, nombre)
values (3000, 'Frutas');

insert into categoria(codigo, nombre)
values (4000, 'Verduras');

insert into categoria(codigo, nombre)
values (5000, 'Lacteos');


--Registros producto
insert into producto(codigobarra, nombre, precio, cantidad, capacidad, tipo)
values (201000,'Smirnoff', 40000, 100, 100, 1000 );

insert into producto(codigobarra, nombre, precio, cantidad, capacidad, tipo)
values (202000,'Costilla', 20000, 100, 100, 2000 );

insert into producto(codigobarra, nombre, precio, cantidad, capacidad, tipo)
values (202001,'Chorizo', 25000, 100, 100, 2000 );

insert into producto(codigobarra, nombre, precio, cantidad, capacidad, tipo)
values (204000,'Tomate', 8000, 100, 100, 4000 );

insert into producto(codigobarra, nombre, precio, cantidad, capacidad, tipo)
values (205000,'Queso Mozarella', 11000, 100, 100, 5000 );


--Registro registroVenta
insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
values (1000000004, 0001, 'Sevillana - 2 costillas BBQ', '2022-08-31');

insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
values (1000000004, 0001, 'Zenu - 6 chorizos rancheros', '2022-08-29');

insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
values (1000000003, 0002, 'Smirnoff - Vodka 750ml', '2022-08-20');

insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
values (1000000003, 0003, 'Smirnoff - Vodka 750ml', '2022-08-26');

insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
values (1000000002, 0002, 'Sevillana - costilla BBQ', '2022-08-28');

insert into registroventa(usuario, idcliente_venta, infoventa, fecha)
values (1000000002, 0002, 'primera insercción de manera automatica', '2022-08-31');

SELECT * FROM registroventa;
--Registros Venta
insert into venta(idventa, idproducto, cantidad)
values (1, 202000, 2);

insert into venta(idventa, idproducto, cantidad)
values (2, 202001, 6);

insert into venta(idventa, idproducto, cantidad)
values (3, 201000, 1);

insert into venta(idventa, idproducto, cantidad)
values (4, 201000, 1);

insert into venta(idventa, idproducto, cantidad)
values (5, 202000, 1);

insert into venta(idventa, idproducto, cantidad)
values (6, 201000, 1);

insert into venta(idventa, idproducto, cantidad)
values (6, 202000, 2);

insert into venta(idventa, idproducto, cantidad)
values (6, 202001, 3);

insert into venta(idventa, idproducto, cantidad)
values (6, 204000, 4);

--Registros provedor y distribuidoras
--Frutas y Verduras
insert into provedor(codigo, nombre)
values(700100, 'Waruwa');

--Licores y Cigarrillos
insert into provedor(codigo, nombre)
values(700101, 'JM Licores');

--Carnes y lacteos
insert into provedor(codigo, nombre)
values(700102, 'Carnes Santacruz');

--Registros producto Ofrecido
insert into prodofrecido(idprovedor, idproducto, preciounitario)
values(700101, 201000, 40000);

insert into prodofrecido(idprovedor, idproducto, preciounitario)
values(700102, 202000, 20000);

insert into prodofrecido(idprovedor, idproducto, preciounitario)
values(700102, 202001, 25000);

insert into prodofrecido(idprovedor, idproducto, preciounitario)
values(700100, 204000, 8000);

insert into prodofrecido(idprovedor, idproducto, preciounitario)
values(700102, 205000, 11000);


