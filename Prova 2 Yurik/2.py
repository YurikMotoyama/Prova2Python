temp1 = [21, 23, 35, 34, 23 ,34 , 12]
temp2 = [25, 13, 15, 14, 13 ,14 , 12]

tupla1 = ("Lavendertown", temp1)
tupla2 = ("Curitibinha do norte", temp2)

listaDeTuplas = [tupla1, tupla2]

def mediaTemp(lista):
    tempMedia = 0
    for item in lista:
        temp = item[1]
        for grau in temp:
            tempMedia += grau
        print("A temp media de" , item[0] , "é", tempMedia/7)
        tempMedia = 0
     

mediaTemp(listaDeTuplas)
