'''
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# isnumeric isdigit isdecimal
# checa números e positivos

if num1.isdigit() and num2.isdigit():

    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)

else:
    print('Não é possível efetuar a operação.')

'''''

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)

except:
    print('Não é possível efetuar a operação.')
