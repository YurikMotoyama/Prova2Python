produto1 = ("banana", 1, 11320.50, 10)
produto2 = ("maçã", 2, 15130.50, 10)
produto3 = ("pera", 3, 5610.50, 10)
produto4 = ("empilhadeira de titanio com capacidade de 7 toneladas", 4, 1.99, 10)

produtos = [produto1,produto2,produto3,produto4]

## A


def criarProduto(listaDeProdutos,nome,codigo,preco,estoque):
    novaTupla = [nome,codigo,preco,estoque]
    novaTupla = tuple(novaTupla)
    return listaDeProdutos.append(novaTupla)


## B


def atualizarEstoque(listaDeProdutos,produto, quantidade):
    stringTuplaNova = []
    for item in produto:
        stringTuplaNova.append(item)
    stringTuplaNova[3] = quantidade
    tuplaNova = tuple(stringTuplaNova)
    if (produto in listaDeProdutos):
        listaDeProdutos.remove(produto)
        listaDeProdutos.append(tuplaNova)
    else:
        print("produto nao encontrado")
    



## C


def listarProdutos(listaDeProdutos):
    for produto in listaDeProdutos:
        print("----------------------")
        print("Nome ", produto[0])
        print("ID ", produto[1])
        print("Preço  ", produto[2])
        print("quantidade ", produto[3])       


## D

criarProduto(produtos, "sasuke",5, 12314,1)

atualizarEstoque(produtos, produtos[2], 20)

listarProdutos(produtos)

        