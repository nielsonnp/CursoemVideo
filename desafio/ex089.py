'''Faça um Programa que peça as três notas de 10 alunos, que devem
ser entre 0 e 100, e calcule e armazene a média de cada aluno. Em
seguida, imprima o número de alunos com média maior ou igual a 70 e
a lista dos alunos e suas médias. Exiba uma mensagem cada vez que
for informado notas inválidas, ou seja, notas negativas ou acima de
100.'''

notas = []
aprovado = 0
reprovado = 0

print('Digite notas de 0 - 100:')

for i in range(0,10):
    nome = input("Qual o seu Nome? ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1+n2+n3)/3
    notas.append([nome,media])
    if (media >= 70):
        aprovado += 1
    else:
        reprovado += 1

print("Números de alunos com média maior ou igual a 70 = {}" .format(aprovado))
print("Nome dos alunos e médias {}".format(notas))