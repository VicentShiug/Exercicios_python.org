# 1. Faça um Programa que peça dois números e imprima o maior deles. 

'''
num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))
print(f'O maior número é {f"o primeiro inserido: {num1}" if num1 > num2 else f"o segundo inserido: {num2}"}')
'''

# 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

'''
num = float(input('Digite um número: '))
print(f'O valor inserido {num} é {"positivo" if num > 0 else "negativo"}')
'''

# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

'''
caracter = str(input('Escolha entre "F" ou "M": '))
print(f'{"Masculino" if caracter == "M" or caracter == "m" else "Feminino" }')
'''


# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 

'''
caracter = input('Insira um caracter: ')
def mensagem():
  return print('É vogal')

if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':
  mensagem()
else:
  print('É uma consoante')
'''

# 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    # a. A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    # b. A mensagem "Reprovado", se a média for menor do que sete;
    # c. A mensagem "Aprovado com Distinção", se a média for igual a dez. 
    
'''
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media < 10:
  print(f'Aluno aprovado, a média é: {media}')
elif media < 7:
  print(f'Aluno reprovado, a média é: {media}')
elif media == 10:
  print(f'Aluno aprovado com distinção, a média é: {media}')
'''

# 6. Faça um Programa que leia três números e mostre o maior deles. 

'''
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))
num3 = float(input('Insira mais outro número: '))

if num1 > num2 and num1 > num3:
  print(f'O maior número foi o primeiro {num1}')
elif num2 > num1 and num2 > num3:
  print(f'O maior número foi o segundo {num2}')
elif num1 == num2 and num2 == num3:
  print(f'segredo massssssss.... os três número são iguais')
else:
  print(f'O maior número foi o terceiro {num3}')
'''
