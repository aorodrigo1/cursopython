nome = 'Rodrigo Oliveira'
idade = 29
altura = 1.76
e_maior = idade > 18  # booleano
peso = 75
imc = peso / (altura ** 2)

print("Nome:", nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print(nome, ' tem', sep=',', end=' ')
print(idade, 'anos e possui um valor calculado de IMC igual a', str(round(imc, 2)), end='.')

#  OU

print('\n' + f'{nome}, tem {idade} anos e possui um valor calculado de IMC igual a {imc:.2f}.')

print('{}, tem {} anos e possui um valor calculado de IMC igual a {:.2f}.'.format(nome, idade, imc))

print('{a}, tem {b} anos e possui um valor calculado de IMC igual a {c:.2f}. Parabéns {a}.'.format(a=nome, b=idade, c=imc))
