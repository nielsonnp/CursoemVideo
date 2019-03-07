frase = "Curso em Vídeo Python"

print(frase[3:13:2]) #Vai de 3 até 13 pulando de 1 em 1
print(frase.count('u')) #Conta quantas vezes tem o 'u' minusculo na variavel frase
print(len(frase)) #Conta quantos tamanhos tem a frase
print(len(frase.strip())) #Remove os espaço em branco
print(frase.upper()) #Coloca a frase em maiuscula
print(frase.replace('Python','Android')) #Substitui Python por Android
print('Curso' in frase) #Se a palavra curso está dentro da frase Vai mostrar True or False
print(frase.find("Vídeo"))#Vai dizer em qual posicao tá a palavra Curso
print(frase.lower().find('vídeo'))#Vai colocar a frase em minusculo e localizar em qual posicao ta o no curso