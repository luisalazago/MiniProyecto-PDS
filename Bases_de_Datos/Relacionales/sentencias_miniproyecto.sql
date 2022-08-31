-- Funcion 1: Retorna la clave del usuario
create or replace FUNCTION retornarclave(numeric)
    RETURNS TABLE (contrasena char) as 
	$$
	BEGIN RETURN QUERY
		SELECT usuario.contrasena 
		FROM usuario 
		WHERE idUsuario = $1;
	END;
	$$
language 'plpgsql';

-- Funcion 2: Retornar la cantidad disponible de un producto
create or replace FUNCTION retornarinvPro(numeric)
    RETURNS TABLE (nombre char(20), cantidad numeric(5), capacidad numeric(5), precio numeric(8)) as
    $$
	BEGIN RETURN QUERY
		SELECT producto.cantidad
		FROM producto 
		WHERE codigoBarra = $1;
	END;
    $$
language 'plpgsql';

-- Funcion 2: Retornar el inventario total de todos los productos
create or replace FUNCTION retornarinv()
    RETURNS TABLE (codigoBarra numeric(15), nombre char(20), precio numeric(8), cantidad numeric(5), tipo char(20)) as
    $$
	BEGIN RETURN QUERY
		SELECT producto.codigoBarra, producto.nombre, producto.precio, producto.cantidad, categoria.nombre
		FROM producto INNER JOIN categoria ON (producto.tipo = categoria.codigo);
	END;
    $$
language 'plpgsql';

-- Funcion 3: Retornar plata (Factura)
create or replace FUNCTION facturar(numeric)
    RETURNS TABLE (nombre char(20), cantidad numeric(5), precio numeric(15)) as
    $$
	BEGIN RETURN QUERY
		SELECT producto.nombre, venta.cantidad, venta.cantidad * producto.precio
		FROM venta INNER JOIN producto on (venta.idProducto = producto.codigoBarra)
		WHERE venta.idVenta = $1;
	END;
    $$
language 'plpgsql';
	
-- Funcion 4: Retornar precio total factura
create or replace FUNCTION total(numeric)
    RETURNS TABLE (precio numeric(15)) as
    $$
	BEGIN RETURN QUERY
		SELECT SUM(venta.cantidad * producto.precio)
		FROM venta INNER JOIN producto on (venta.idProducto = producto.codigoBarra)
		WHERE venta.idVenta = $1;
	END;
    $$
language 'plpgsql';
	
-- Funcion 5: Retornar info reporte
create or replace FUNCTION reporteDiario()
    RETURNS TABLE (nombre char(20), cantidad numeric(7), precio numeric(15), tipo char(20)) as
    $$
	BEGIN RETURN QUERY
		WITH suma AS (SELECT producto.nombre as nombre, SUM(venta.cantidad) as cantidad 
				FROM (producto INNER JOIN venta on (venta.idProducto = producto.codigoBarra))
				INNER JOIN registroVenta on (registroVenta.idRegistro = venta.idVenta) 
				WHERE registroVenta.fecha = (SELECT CURRENT_DATE)
				GROUP BY producto.nombre)
		SELECT suma.nombre, suma.cantidad, suma.cantidad*producto.precio, categoria.nombre
		FROM (suma INNER JOIN producto USING (nombre)) INNER JOIN categoria ON (producto.tipo = categoria.codigo);
	END;
    $$
language 'plpgsql';
	
-- Funcion 6: Retornar total reporte
create or replace FUNCTION reporteDiarioTotal()
    RETURNS TABLE (precioReporte numeric(15)) as
    $$
	BEGIN RETURN QUERY
	SELECT SUM(precio) FROM reporteDiario();
	END;
    $$
language 'plpgsql';

--Pruebas y Consultas

--Retornar la cantidad disponible de un producto
SELECT * FROM retornarinv (201000);

--Retornar el registro de venta de una venta
SELECT * FROM facturar(301004);

--Retornar toda la información de venta
SELECT * FROM venta;

--Retornar total de la factura
SELECT * FROM total (301004);

--Retornar reporte diario
SELECT * FROM reporteDiario();

--Retornar reporte diario total
SELECT * FROM reportediariototal();
