"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com chaves)

pessoa: Britney Spears

"""""

nome = 'Britney Spears'
idade = 40
altura = 1.63
peso = 58.9
ano_atual = 2021  # ano atual seria 2022, mas para o cálculo correto 2021
ano_nasc = ano_atual - idade
imc = peso / altura ** 2

print('{0} tem {1} anos, {2} de altura e pesa {3}kg.'.format(nome, idade, altura, peso))
print('O IMC de {i} é {j:.2f}.'.format(i=nome, j=imc))
print('{} nasceu em {}.'.format(nome, ano_nasc))

num_1 = 2
num_2 = '2'
## num_3 = num_2 + num_1

## print(num_3)