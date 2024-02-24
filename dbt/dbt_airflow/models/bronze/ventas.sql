{{ config(materialized='table') }}

SELECT
    "IdVenta" as id_venta,
    "Fecha" as fecha,
    "Fecha_Entrega" as fecha_entrega,
    "IdCanal" as id_canal,
    "IdCliente" as id_cliente,
    "IdSucursal" as id_sucursal,
    "IdEmpleado" as id_empleado,
    "IdProducto" as id_producto,
    "Precio" as precio,
    "Cantidad" as cantidad
FROM venta