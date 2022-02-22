"""""
COMANDOS = Iniciar com letra, pode conter números, separar _, letras mínusculas
"""""

#  nome = 'Rodrigo'
#  print(nome, type(nome))

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
print(3 * '\n' + 'BLABLABLA')