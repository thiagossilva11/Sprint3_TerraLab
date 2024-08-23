import moeda 

p = float(input("Digite o preço:R$: "))
print(f"A metade do preço de {(p)} é {moeda.metade(p)}")
print(f"O dobro do preço de {(p)} é {moeda.dobro(p)}")
print(f"Aumentando em 10%, temos que o {(p)} ajustado é de {moeda.aumentar(p,10)}")
print(f"Diminuindo em 20%, temos que o {(p)} ajustado é de {moeda.diminuir(p,20)}")
