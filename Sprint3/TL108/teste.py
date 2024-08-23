import moeda
p= float(input("Digite o preço:R$: "))
print(f"A metade do preço de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}")
print(f"O dobro do preço de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando em 10%, temos que o {moeda.moeda(p)} ajustado é de R$ {moeda.moeda(moeda.aumentar(p,10))}")
print(f"Diminuindo em 20%, temos que o {moeda.moeda(p)} ajustado é de R$ {moeda.moeda(moeda.diminuir(p,20))}")

