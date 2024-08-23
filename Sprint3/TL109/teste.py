import moeda
p= float(input("Digite o preço:R$: "))
print(f"A metade do preço de {moeda.moeda(p)} é {(moeda.metade(p,True))}")
print(f"O dobro do preço de {moeda.moeda(p)} é {(moeda.dobro(p,True))}")
print(f"Aumentando em 10%, temos que o {(p)} ajustado é de  {(moeda.aumentar(p,10,True))}")
print(f"Diminuindo em 20%, temos que o {(p)} ajustado é de  {(moeda.diminuir(p,20,True))}")

