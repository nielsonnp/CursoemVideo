lanche = ("Hamburgue", "Suco", "Pizza", "Pudin")

for cont in range(0, len(lanche)): #O (lanche[cont]) imprime um abaixo do outro e (cont) imprime as posicoes em numeros um abaixo do outro
    print("Eu vou comer {} na posição {} ".format(lanche[cont], cont))

print(lanche) #Mostra a lista em ordem inicial
print(sorted(lanche)) #O sorted coloca em ordem alfabetica
print(lanche.index('Pizza'))# Mostra em qual posição tá o nome pizza
print(lanche.count('Pizza')) # Mostra quantos nomes pizzas tem