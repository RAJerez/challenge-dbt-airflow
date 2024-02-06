

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