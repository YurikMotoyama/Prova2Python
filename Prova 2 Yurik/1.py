print("teste")

def palindromo():
    inputDoUsuario = input("Coloca a palavra ai pfv: ")
    outraPalavrinha = []
    for caracter in inputDoUsuario:
        outraPalavrinha.append(caracter)
    outraPalavrinha.reverse()
    conferir = ""
    for caracter in outraPalavrinha:
        conferir += caracter
    print(conferir)
    if(conferir == inputDoUsuario):
        print("é")
    else:
        print("nao é")

palindromo("arara")
palindromo("One Step Closer - Linkin Park")
