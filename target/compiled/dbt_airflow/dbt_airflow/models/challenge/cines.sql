-- Antes hay que crear las siguientes columnas: telefono y mail



select
    "cod_localidad" as cod_localidad,
    "id_provincia" as id_provincia,
    "id_departamento" as id_departamento,
    "provincia" as provincia,
    "categoria" as categoria,
    "direccion" as domicilio,
    "cp" as codigo_postal,
    "localidad" as localidad,
    "nombre" as nombre,
    NULL as telefono,
    NULL as mail,
    "web" as web
FROM raw_cine