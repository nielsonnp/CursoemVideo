'''Imprimir o nome maiúsculo e minúsculo, quantas letras tem seu nome sem espaço
e quantas letras tem seu primeiro nome'''
nome = input("Digite seu nome completo: ").strip() #Strip elimina os espaço

print('Seu nome maiúsculo é {}'.format(nome.upper()))
print('Seu nome minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#Outra forma de achar o primeiro nome e contar quantas letras tem
separa = nome.split() #O split joga dentro de uma lista os nomes interios
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))