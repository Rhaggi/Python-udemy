n1 = n2 = 0.0
media = 0.0

faltas = int(input('Digite a quantidade de faltas:'))
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

# Calcular média aritmetica

media = (n1 + n2) / 2

if(faltas >= 10): 
    print('Reprovado por faltas!')  
elif(media > 7):
    print("Aprovado! Sua nota é ", media)
elif(media == 5):
    print('Voce esta de recuperação, sua média é {media}')
else: 
    print('Reprovado com média ', media)

