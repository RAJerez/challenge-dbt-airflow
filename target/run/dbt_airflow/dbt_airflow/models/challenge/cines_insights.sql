
  
    

  create  table "data-challenge-dbt"."public"."cines_insights__dbt_tmp"
  
  
    as
  
  (
    

SELECT 
"provincia" AS provincia,
SUM("pantallas") AS pantallas,
SUM("butacas") AS butacas,
COUNT(CASE WHEN "espacio_incaa" = 'Si' THEN 1 END) AS espacios_incaa
FROM raw_cine
GROUP BY "provincia"


/*
COLUMNAS raw_cine
'cod_localidad', 'id_provincia', 'id_departamento', 'categoria',
'provincia', 'departamento', 'localidad', 'nombre', 'direccion', 'piso',
'cp', 'web', 'latitud', 'longitud', 'tipo_latitud_longitud', 'fuente',
'sector', 'pantallas', 'butacas', 'tipo_de_gestion', 'espacio_incaa',
'año_actualizacion'
*/
  );
  