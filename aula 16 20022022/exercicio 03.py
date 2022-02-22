'''
Faça um programa que peça primeiro o nome do usuário.
Se tiver 4 letras ou menos escreva: Seu nome é curto.
Entre 5-6 letras: Seu nome é normal.
Maior que 6: Seu nome é grande.
'''''

nome = input('Qual é o seu nome? ')
carac_nome = len(nome)

if carac_nome <= 4:
    print('Ha! Seu nome é pequeno.')
elif carac_nome <= 6:
    print('Uh! Seu nome é normal.')
elif carac_nome > 6:
    print('Uau! Seu nome é grande.')
