import pymysql

# Conexão com o banco de dados
conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='06101989',
    database='db_vendas'
)

cursor = conexao.cursor()

# Lista de queries e seus títulos
queries = [
    ("Total de vendas", "SELECT SUM(Valor * Quantidade) AS Total_Vendido FROM vendas"),
    ("Total de itens vendidos", "SELECT SUM(Quantidade) AS Total_Itens_Vendidos FROM vendas"),
    ("Ticket médio por venda", "SELECT SUM(Valor * Quantidade) / COUNT(DISTINCT Venda_ID) AS Ticket_Medio FROM vendas"),
    ("Top 5 produtos mais vendidos", """
        SELECT Produto, SUM(Quantidade) AS Total_Quantidade
        FROM vendas
        GROUP BY Produto
        ORDER BY Total_Quantidade DESC
        LIMIT 5
    """),
    ("Categoria com maior volume de vendas", """
        SELECT Categoria, SUM(Quantidade) AS Total_Quantidade
        FROM vendas
        GROUP BY Categoria
        ORDER BY Total_Quantidade DESC
        LIMIT 1
    """),
    ("Cliente que mais comprou", """
        SELECT Cliente_ID, SUM(Valor * Quantidade) AS Total_Comprado
        FROM vendas
        GROUP BY Cliente_ID
        ORDER BY Total_Comprado DESC
        LIMIT 1
    """)
]

# Executando cada query e exibindo resultados
for titulo, sql in queries:
    print(f"\n--- {titulo} ---")
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for linha in resultados:
        print(linha)

# Fechar conexão
cursor.close()
conexao.close()