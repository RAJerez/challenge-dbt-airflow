
  
    

  create  table "data-challenge-dbt"."public"."size_by_category_province__dbt_tmp"
  
  
    as
  
  (
    

WITH categorias AS (
    SELECT categoria, provincia
    FROM "data-challenge-dbt"."public"."cines"
    UNION ALL
    SELECT categoria, provincia
    FROM "data-challenge-dbt"."public"."museos"
    UNION ALL
    SELECT categoria, provincia
    FROM "data-challenge-dbt"."public"."bibliotecas"
)

SELECT
    categoria,
    provincia,
    COUNT(*) AS cantidad
FROM categorias
GROUP BY categoria, provincia
  );
  