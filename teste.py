'''import emoji
print(emoji.emojize('olá Mundo :earth_americas:', use_aliases=True))'''

'''import random
num = random.randint(0, 4)

nomes = ['Ranyelson', 'Ana', 'Marianna', 'Melissa']

print(nomes[num])'''

import random

j1 = input('(1° jogador) Digite seu nome: ')
j2 = input('(2° jogador) Digite seu nome: ')
j3 = input('(3° jogador) Digite seu nome: ')

sort = random.randint(1,3)

if sort == 1:
    print('Parabéns',j1,'Você Ganhou!!')
elif sort == 2:
    print ('Parabéns',j2,'Você Ganhou!!')
elif sort == 3:
    print ('Parabéns',j3,'Você Ganhou!!')