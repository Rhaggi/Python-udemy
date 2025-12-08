import math

nome = 'rosa'
idade = 23
casada = True

x = y = z = 0

x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

z = x + y
a = x * y
b = x/y
c = x%y
d = math.pow(x,y)

print('A soma dos números é ', z)
print('A multiplicação dos números é ', a)
print('A divisão dos números é ', b)
print('O módulo dos números é ', c)
print('O primeiro número elevado ao segundo é ', d)