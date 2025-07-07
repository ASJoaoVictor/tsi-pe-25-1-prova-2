from random import randint

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
def ler_valores():
    lista = []
    while True:
        n = int(input("Digite um número(Digite 0 para parar): "))
        if(n == 0):
            break
        lista.append(n)
    return lista
def q3(valores):#É a função processa_lista(lista)
    par = []
    impar = []
    for valor in valores:
        if(valor % 2 == 0):
            par.append(valor)
        else:
            impar.append(valor)
    return  par, impar

def ler_03_alturas():
    alturas = []
    for i in range(0, 3):
        altura = float(input("Digite o valor da altura: "))
        alturas.append(altura)
    return alturas

#Solução simples
def q4_2(valores:list):
    valores.sort()
    alturas_sort = [valores[1],valores[2],valores[0]]
    return alturas_sort

def q4(valores:list):
    alturas_sort = []

    maior = medio = menor = valores[0]
    for i in range(len(valores) -1 , -1, -1):
        for valor in valores:
            if(valor <= menor):
                menor = valor
            elif(valor >= maior):
                maior = valor
            else:
                medio = valor
    alturas_sort = [f"{medio:.2f}", f"{maior:.2f}", f"{menor:.2f}"]

    return alturas_sort


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

    lista =  ler_valores();
    resultado = q3(lista)
    print(f"q2: {resultado}")

    alturas = ler_03_alturas();
    print("q4: ", q4(alturas))
    print("q4: ", q4_2(alturas))


if __name__ == "__main__":
    main()


