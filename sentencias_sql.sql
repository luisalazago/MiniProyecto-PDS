-- Traer contraseña
create or replace FUNCTION retornarclave(numeric)
    RETURN char as
    'SELECT contrasena 
    FROM Usuario 
    WHERE idUsuario = $1;'
    language sql;

-- Traer inventario
create or replace FUNCTION retornarinv(numeric)
    RETURN numeric as
    'SELECT cantidad 
    FROM producto 
    WHERE codigoBarra = $1;'
    language sql;

-- Plata 
SELECT producto.nombre as Nombre, venta.cantidad as Cantidad, venta.cantidad * producto. precio as precio
FROM venta INNER JOIN producto on (venta.idProducto = producto.codigoBarra)
WHERE venta.idVenta = x;

-- Plata total
SELECT SUM(venta.cantidad * producto) as Total
FROM venta INNER JOIN producto on (venta.idProducto = producto.codigoBarra)
WHERE venta.idVenta = x;


