# 1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.

'''
print("Alo mundo")
'''

# 2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

'''
numero = input('Digite um número: ')
print(f'O número informadoo foi {numero}')
'''

# 3. Faça um Programa que peça dois números e imprima a soma.

'''
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite o segundo numero: '))
print(f'A soma é: {num1 + num2}')
'''

# 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

'''
nota1 = int(input('digite a nota1: '))
nota2 = int(input('digite a nota2: '))
nota3 = int(input('digite a nota3: '))
nota4 = int(input('digite a nota4: '))

print(f'A média é {(nota1 + nota2 + nota3 + nota4) / 4}')
'''

# 5. Faça um Programa que converta metros para centímetros.

'''
metros = float(input('Digite a metragem: '))
centimetro = metros * 100
print(f'{metros} metros é igual a {centimetro} centímetros')
'''

# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

'''
raio = float(input('digite o raio: '))
area = 3.14 * (raio**2)
print(f'A área é: {area}cm²')
'''

# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''
lado = float(input('Insira o lado do quadrado: '))
area = lado**2
area_ao_dobro = area*2
print(f'A área é: {area} e o quadrado da área é: {area_ao_dobro}')
'''

# 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

'''
salario_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_por_mes = int(input('Digite quantas horas você trabalha por mẽs: '))
total = (salario_por_hora * horas_por_mes) * 22
print(f'O total ganho por mês é igual a: {total}')
'''

# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

'''
fahrenheit = float(input('Digite uma temperatura em graus Fahrenheit: '))
celsius = 5 * ((fahrenheit-32) / 9)
print(f'A temperatura {fahrenheit} fh em Calsius é {celsius}')
'''

# 10.  Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

'''
celsius = float(input('Digite uma temperatura em graus Celsius: '))
f = celsius * 1.8 + 32
print(f'A temperatura {celsius} c em Fahrenheit é {f}')
'''

# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

'''
int1 = int(input('Insira um número inteiro: '))
int2 = int(input('Insira outro número inteiro: '))
real = float(input('Insira um número real: '))
  # a. o produto do dobro do primeiro com metade do segundo . 
  # O produto é o resultado de uma multiplicação
  
produto = (int1 * 2) * (int2 / 2)
print(f'O produto do dobro do primeiro com metade do segundo é: {produto}')
  
  # b. a soma do triplo do primeiro com o terceiro. 

asoma = (int1 * 3) + real
print(f'A soma do triplo do primeiro com o terceiro é: {asoma} ')

  # c. o terceiro elevado ao cubo. 

cubo = real **3
print(f'o terceiro elevado ao cubo é {cubo}')
'''

# 12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

'''
altura = float(input('Digite sua altura: '))
peso_ideal = (72.7 * altura) - 58
print(f'Seu peso ideal é: {peso_ideal}')
'''

# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

'''
h = float(input('Digite sua altura: '))

  # a. Para homens: (72.7*h) - 58

peso_ideal_homem = (72.7 * h) - 58
print(f'Seu peso ideal, caso seja homem, é: {peso_ideal_homem}')

  
  # b. Para mulheres: (62.1*h) - 44.7 

peso_ideal_mulher = (62.1 * h) - 44.7
print(f'Seu peso ideal, caso seja homem, é: {peso_ideal_mulher}')
'''

# 14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de 
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que 
# leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do 
# limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

'''
limite = 50
peso = float(input('Insira o peso do peixe pescado: '))
excesso = peso - limite
multa = 0
if(excesso < 0):
    pass
else:
  multa = excesso * 4

print(f'Você devera pagar R${multa} de multa')
'''

# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 
# 5% para o sindicato, faça um programa que nos dê:
'''
salario_hora = float(input('Quanto você ganhar por hora: '))
hora_mes = float(input('Quantas horas você trabalha por mês: '))

total_salario_bruto = (salario_hora * hora_mes)  * 22
imposto_renda = 11/100 * total_salario_bruto
inss = 8/100 * total_salario_bruto
sindicato = 5/100 * total_salario_bruto
total_salario_liquido = total_salario_bruto - imposto_renda - inss - sindicato

#a. salário bruto.
    #b. quanto pagou ao INSS.
    #c. quanto pagou ao sindicato.
    #d. o salário líquido.
    #e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

    # + Salário Bruto : R$
    # - IR (11%) : R$
    # - INSS (8%) : R$
    # - Sindicato ( 5%) : R$
    # = Salário Liquido : R$

    # Obs.: Salário Bruto - Descontos = Salário Líquido. 
'''
# print(f'''
#       + Salário Bruto   : R$ {total_salario_bruto}
#       - IR        (11%) : R$ {imposto_renda}
#       - INSS      (8%)  : R$ {inss}
#       - Sindicato (5%)  : R$ {sindicato}
#       = Salário Liquido : R$ {total_salario_liquido}
#       ''')

# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 

'''
metros = float(input('Insira, metros quadrados, a área a ser pintada: '))
latas = 1
if (metros > 54):
  latas = round((metros / 54) + 0.5)
gasto = latas * 80
print(f'Latas a serem compradas: {latas}, preço total: {gasto}')
'''

# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

'''
metros = float(input('Insira, metros quadrados, a área a ser pintada: '))
litros = ((metros / 6) * 1.1) # acressentando 10%
latas = 1
galoes = 1

#  1 lata cobre 108 metros
#  1 galão cobre 21,6 metros
    # - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    # a. comprar apenas latas de 18 litros;

if (metros > 108):
  latas = round((metros / 108) + 0.5)
gst_latas = latas * 80

print(f'Quantidade de latas: {latas}, o total gasto é: {gst_latas}')

    # b. comprar apenas galões de 3,6 litros;

if (metros > 21.6):
  galoes = round((metros / 21.6) + 0.5)
gst_galoes = galoes * 25
print(f'Quantidade de galões: {galoes}, o total gasto é: {gst_galoes}')
    
    
    # c. misturar latas e galões, de forma que o desperdício de tinta seja menor. 
    #    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

mix_latas = round(litros / 18)
mix_galoes = round((litros - mix_latas * 18) / 3.6)

if ((litros - (mix_latas * 18) % 3.6 != 0)):
  mix_galoes += 1
  total_mix = (mix_latas * 80) + (mix_galoes * 25)

print(f'Misturando para melhor eficiencie ficaria com a quantidade de galões: {mix_galoes},  quantidade de latas: {mix_latas} e o total gasto é: {total_mix}')
'''

# 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos). 

'''
tamanho = float(input('Digite o tamanho do arquivo (em MB): '))
velocidade = float(input('Digite a velocidade da internet (em Mbps): '))
tempo = (tamanho / (velocidade / 8)) / 60

print(f'O tempo aproximado de donwload do arquivo usando esta conexão é: {tempo} minutos')
'''



    
    
