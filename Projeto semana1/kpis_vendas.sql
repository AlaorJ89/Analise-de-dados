-- Total de vendas
SELECT SUM(Valor) FROM vendas;

-- Total de itens vendidos
SELECT SUM(Quantidade) FROM vendas;

-- Ticket médio por venda
SELECT SUM(Valor)/COUNT(DISTINCT Venda_ID) FROM vendas;

-- Top 5 produtos mais vendidos
SELECT Produto, SUM(Quantidade) FROM vendas GROUP BY Produto ORDER BY SUM(Quantidade) DESC LIMIT 5;

-- Categoria com maior volume de vendas
SELECT Categoria, SUM(Quantidade) FROM vendas GROUP BY Categoria ORDER BY SUM(Quantidade) DESC LIMIT 1;

-- Cliente que mais comprou
SELECT Cliente_ID, SUM(Valor) FROM vendas GROUP BY Cliente_ID ORDER BY SUM(Valor) DESC LIMIT 1;
