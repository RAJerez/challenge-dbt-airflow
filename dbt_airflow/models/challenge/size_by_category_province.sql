{{ config(materialized='table') }}

WITH categorias AS (
    SELECT categoria, provincia
    FROM {{ ref('cines') }}
    UNION ALL
    SELECT categoria, provincia
    FROM {{ ref('museos') }}
    UNION ALL
    SELECT categoria, provincia
    FROM {{ ref('bibliotecas') }}
)

SELECT
    categoria,
    provincia,
    COUNT(*) AS cantidad
FROM categorias
GROUP BY categoria, provincia