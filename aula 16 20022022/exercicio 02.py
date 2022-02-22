'''
Faça um programa que pergunte a hora  ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada (bom dia, boa tarde, boa noite).
'''''

hora = input('Digite a hora: ')

if hora.isnumeric():

    hora_int = int(hora)

    if hora_int < 0 or hora_int > 23:
        print('Hora deve ser entre 0 e 23.')
    else:
        if hora_int <= 11:
            print('Bom dia!')
        elif hora_int <= 17:
            print('Boa tarde!')
        elif hora_int <= 23:
            print('Boa noite!')

else:
    print('A hora digitada não é válida, digite apenas o número.')