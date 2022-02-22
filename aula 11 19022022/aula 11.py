'''
Operadores Relacionais
== > >= < <= !=

!= diferente
'''''
'''
var_1 = 'Rodrigo'
var_2 = 'Oliveira'

expressao = var_1 != var_2

print(expressao)

'''

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)  # INPUT SEMPRE CONVERTE STRING

# Limite para pegar empréstimo
idade_menor = 20  # jovem
idade_maior = 30  # passou da idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')


