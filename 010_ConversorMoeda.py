real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))

'''O primeiro é ja deixando o valor fixo do dolar e o segundo 
   é quando pede pra o usuario digitar o valor do dolar'''

'''real = float(input('Digite quanto você tem em Reais? R$'))
dolar = float(input('Digite o valor do Dólar? US$'))
conversao = real / dolar
print('Com R${:.2f} e o dolar a US${:.2f} você pode comprar US${:.2f}'.format(real, dolar, conversao))'''