import os
os.system("cls")
print(" Exercício 1 - Lista de 10 números")
lista = []
lista2 = []
for cont in range (1, 11):
    n = int(input(f"Insira o {cont}° número: "))
    lista.append(n)
    if n > 15:
        lista2.append(n)
print(f"{lista2}")
 
 
print("Exercício 2 - Programa com lista de 8 números")
lista3 = []
lista4 = []
for cont in range (1,9):
    n = int(input(f"Digite o {cont}° número: "))
    lista3.append(n)
    if n % 3 == 0 :
        lista4.append(n)
print(f"{lista4}")
 
print("Exercício 3 - Programa com lista de 9 números e soma")
lista5 = []
lista6 = []
for cont in range (1,10):
    n = int(input(f"Digite o {cont}° número: "))
    lista5.append(n)
    if n % 2 == 0:
        lista6.append(n)
        x = sum(lista6)
print(f"{x}")
 
print("Exercício 4 - Lista de 12 números e imprimir os de posição ímpar")
lista7 = []
for cont in range (1,13):
    n = int(input(f"Digite o {cont}° número: "))
    lista7.append(n)
print(lista7[0:13:2])
 
print("Exercício 5 - Lista de 10 números e gerar uma nova lista com números quadrados")
lista8 = []
lista9 = []
for cont in range (1,11):
    n = int(input(f"Digite o {cont}° número: "))
    lista8.append(n)
    lista9.append(n * n)
print(f"{lista9}")
 
print("Exercício 6 - Lista de 15 números inteiros e mostre quantas vezes o 0 é repetido")
lista10 = []
lista11 = []
for cont in range (1,16):
    n = int(input(f"Digite o {cont}° número: "))
    lista10.append(n)
    x = lista10.count(0)
print(f"{x}")
 
