

WITH categorias AS (
    SELECT categoria FROM cines
    UNION ALL
    SELECT categoria FROM museos
    UNION ALL
    SELECT categoria FROM bibliotecas
)

SELECT
    categoria,
    COUNT(*) AS cantidad
FROM categorias
GROUP BY categoria