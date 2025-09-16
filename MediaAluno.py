nome = input('Digite seu nome: ')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
media = (n1 + n2 + n3) / 3
print('Sua média foi ',media)
if media >= 7:
    print(nome,'foi aprovado por média!!!')
elif media < 7 and media >= 5:
    print(nome,"vai fazer prova final!!!")
else:
    print(nome,"foi reprovado.")