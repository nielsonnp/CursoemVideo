'''072 - Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso
de zero até vinte. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostrar por
extenso.'''

cont = ("zero", "um", "dois", "tres", "quatro", "cinco",
        "seis", "sete", "oito", "nove", "dez",
        "onze", "dose", "treze", "catorze", "quinze",
        "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    num = int(input("Digite um número de 1 a 20: "))
    if 0 <= num <= 20:
        break
    print('Tente novamente. ', end='')

print('Você digitou o número {}' .format(cont[num]))