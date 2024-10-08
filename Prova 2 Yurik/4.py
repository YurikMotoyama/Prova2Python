def processar_dados():
    produtos = [
        ("arroz", 5.5, 10),
        ("Feijão", 7.25, 8),
        ("macarrao", 3.20, 15),
    ]

    totalEstoque = sum(produto[2] for produto in produtos)
    precosAcimaDaMedia = [produto[0] for produto in produtos
        if produto[1]> (sum(produto[1] for produto in produtos)/ len(produtos))]
    return totalEstoque, precosAcimaDaMedia

estoqueTotal, produtosMaisCaros = processar_dados()

print("estoque total:", estoqueTotal)
print("estoque total:", produtosMaisCaros)