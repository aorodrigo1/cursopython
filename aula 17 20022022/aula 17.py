#  Modificaodores ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
#  print('{:.2f}'.format(divisao))
#  OU

print(f'{divisao:.2f}')

nome = 'Rodrigo'
print(f'{nome:s}')

'''''

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print(f'{num_2:0>10.2f}')

nome = 'Rodrigo'
#  print ('{n}{n}{n}'.format(n=nome))
print('{:@>4}'.format(nome))  # preenche caracteres conforme eu for aumentando o numero >4>5 ex

nome1 = 'Rodrigo'
nome2 = 'Oliveira'
nome3 = 'Alves'

nome_formatado = '{:!^11} {:!^12} {:!^13}'.format(nome1, nome2, nome3)
print(nome_formatado)

nome_a = 'rOdriGO OliVEIra aLVES'

print(nome_a.lower())
print(nome_a.upper())
print(nome_a.title())
