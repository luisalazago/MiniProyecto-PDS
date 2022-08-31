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
insert into registroventa(idregistro, usuario, idcliente_venta, infoventa, fecha)
values (301000, 1000000004, 0001, 'Sevillana - 2 costillas BBQ', '2022-08-29');

insert into registroventa(idregistro, usuario, idcliente_venta, infoventa, fecha)
values (301001, 1000000004, 0001, 'Zenu - 6 chorizos rancheros', '2022-08-29');

insert into registroventa(idregistro, usuario, idcliente_venta, infoventa, fecha)
values (301002, 1000000003, 0002, 'Smirnoff - Vodka 750ml', '2022-08-20');

insert into registroventa(idregistro, usuario, idcliente_venta, infoventa, fecha)
values (301003, 1000000003, 0003, 'Smirnoff - Vodka 750ml', '2022-08-26');

insert into registroventa(idregistro, usuario, idcliente_venta, infoventa, fecha)
values (301004, 1000000002, 0002, 'Sevillana - costilla BBQ', '2022-08-28');

--Registros Venta
insert into venta(idventa, idproducto, cantidad)
values (301000, 202000, 2);

insert into venta(idventa, idproducto, cantidad)
values (301001, 202001, 6);

insert into venta(idventa, idproducto, cantidad)
values (301002, 201000, 1);

insert into venta(idventa, idproducto, cantidad)
values (301003, 201000, 1);

insert into venta(idventa, idproducto, cantidad)
values (301004, 202000, 1);


