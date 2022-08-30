
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
create or replace FUNCTION retornarinv(numeric)
    RETURNS TABLE (cantidad numeric(5)) as
    $$
	BEGIN RETURN QUERY
		SELECT producto.cantidad
		FROM producto 
		WHERE codigoBarra = $1;
	END;
    $$
    language 'plpgsql';

--Funcion 3: Retornar plata (Factura)
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

--Prueba Consultas
--Retornar la cantidad disponible de un producto
SELECT * FROM retornarinv (201000);

--Retornar el registro de venta de una venta
SELECT * FROM facturar(301004);

--Retornar toda la información de venta
SELECT * FROM venta;


-- Plata total
SELECT SUM(venta.cantidad * producto.precio) as Total
FROM venta INNER JOIN producto on (venta.idProducto = producto.codigoBarra)
WHERE venta.idVenta = 301004;