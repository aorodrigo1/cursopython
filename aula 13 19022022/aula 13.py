'''
usuario = input('Digite seu usuário: ')
qtd_carac = len(usuario)

if qtd_carac < 6:
    print('Digite pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')

'''''

string1 = input('Digite seu primeiro nome: ')
string2 = input('Digite seu segundo nome: ')
string3 = input('Digite seu terceiro nome, se houver: ')

print(f'A quantidade total de caracteres foi de {string1.__len__() + len(string2) + len(string3)}.')