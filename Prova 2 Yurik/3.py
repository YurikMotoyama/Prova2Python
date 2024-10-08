numeros = [1,2,3,4,5,6,7,8,9,10]

def verificaPrimos(lista):
    primosPrimordiais = [1,2,3,5,7]
    for n in lista:
        if(n % 2 == 0):
            if(n == 2):
                print(n, "é primo")
            else:
                (print(n, " n é primo"))
        elif(n % 5 == 0):
            if(n == 5):
                print(n, "é primo")
            else:
                (print(n, " n é primo"))
        elif(n % 7 == 0):
            if(n == 7):
                print(n, "é primo")
            else:
                (print(n, " n é primo"))
        else:
            print(n, " é primo")

verificaPrimos(numeros)