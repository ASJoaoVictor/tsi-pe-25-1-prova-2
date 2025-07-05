def q1(cidades):
    lista = []
    for cidade in cidades:
        if(cidades[cidade] > 100):
            lista.append(cidade)
    return lista 

def q2(lista1, lista2):
    soma = 0
    lista = []

    for i in lista1:
        if i > 0:
            soma += i #soma ao total
            lista.append(i) #adiciona a lista
    for i2 in lista2:
        if i2 > 0:
            soma += i2
            lista.append(i2)
    lista.sort()
    return soma, lista

def q3(valores):
    return [],[]

def q4(valores):
    return []

def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    main()


