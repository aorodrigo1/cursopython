'''
Operadores lógicos
and, or, not
in e not in
'''''

'''
a = 2
b = 3

if not b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')
    
'''

'''
nome = 'Rodrigo Oliveira'

if 'o' in nome:
    print("Existe a letra O no seu nome.")

if 'h' not in nome:
    print("Não existe a letra H no seu nome. ")

'''


usuario = input('Nome de usuário: ')
senha = input('Senha: ')

usuario_bd = 'britneyspears'
senha_bd = 'gimmemore'

if usuario_bd == usuario and senha_bd == senha:
    print('Bem-vindo!')
elif usuario_bd == usuario and senha_bd != senha:
    print('Senha inválida.')
elif usuario_bd != usuario and senha_bd == senha:
    print('Usuário inválido.')
else:
    print('Tente novamente.')
