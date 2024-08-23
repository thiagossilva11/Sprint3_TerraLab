#Exercício  Python 096: Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

#Função área
def area(larg,comp):
    a = larg * comp
    print(f"A área de um terreno com largura {l} e comprimeiro {c} é {a} m^2")




#Programa Principal
print("Controle de Terrenos")
print("-"*20)
l = float(input("Largura(m): "))
c = float(input("Comprimento(m):"))
area(l,c)

    
    