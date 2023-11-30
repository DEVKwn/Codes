import os
os.system ("cls")
print("Programa que recebe o número do operário, o número de peças, sexo do funcionário e mostre um relatório geral. ")
num_operarios = 15
tot_folha = 0
tot_pecas = 0   
media_m = 0
media_f = 0
cont_m = 0
cont_f = 0
SM = 724.00
salario_maior = 0
for cont in range (1, 15 +1, 1):
    numero_operario = int(input("Digite o número do operário: "))
    while numero_operario < 0 or numero_operario > 15:
        numero_operario = int(input("Digite corretamente o número do operário de 1 á 15: "))
    pecas_fabricadas = int(input("Digite o número de peças fabricadas no mês: "))
    while pecas_fabricadas < 0:
        pecas_fabricadas = int(input("Digite o número válido de peças fabricadas no mês: "))
    sexo = input("Digite o sexo do funcionário (M/F): ").upper()
    while sexo != "M" and sexo != "F":
        sexo = input("Digite o sexo correto do funcionário (M/F): ").upper()
    if pecas_fabricadas <= 30:
        salario_op = SM
    elif pecas_fabricadas > 30 and pecas_fabricadas <= 35:
        salario_op = SM + ((pecas_fabricadas - 30)*3/100*SM)
    else:
        pecas_fabricadas > 35
        salario_op = SM + ((pecas_fabricadas - 30)*5/100*SM)
    print(f"Operário número {numero_operario}, salário de R${salario_op:.2f}.")
    input("Pressione ENTER para continuar.")
    os.system("cls")
    tot_folha = tot_folha + salario_op
    tot_pecas = tot_pecas + pecas_fabricadas
    if sexo == "M":
        media_m = media_m + pecas_fabricadas
        cont_m = cont_m + 1
    else:
        media_f = media_f + pecas_fabricadas
        cont_f = cont_f + 1
    if cont == 1:
        salario_maior = salario_op
        num_maior = numero_operario
    else:
        if salario_op > salario_maior:
            salario_maior = salario_op
            num_maior = numero_operario
if cont_m == 0:
    media_m = 0
else:
    media_m = media_m / cont_m
if cont_f == 0:
    media_f = 0
else:
    media_f = media_f / cont_f
print(f"====RELATÓRIO GERAL FÁBRICA==== \n | O total da folha de pagamentos da fábrica foi de R${tot_folha:.2f}.\n | O total de peças fabricadas no mês foram de {tot_pecas} peças.\n | A média de peças fabricas pelos homens foi de {media_m} peças.\n | A média de peças fabricadas pelas mulheres foi de {media_f} peças.\n | O operário(a) com o maior salário foi o número {num_maior}.")
            
        
        
        
    
        
        
