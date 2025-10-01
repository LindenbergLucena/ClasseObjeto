# Escreva um programa que receba uma frase do usuário e conte quantas palavras ela possui.
# Em seguida, inverta a ordem das palavras na frase.
# Revendo sobre manipulação de strings
def processar_frase():
    # Recebe a frase digitada pelo usuário
    frase_original = input('Digite uma frase: ')

    # Divide a frase em listas de palavras
    # O método .split() separa a string por espaços em branco por padrão
    palavras = frase_original.split()

    # Conta o número de palavras:
    numero_de_palavras = len(palavras)

    # Inverte a ordem das palavras na frase:
    palavras_invertidas = palavras[::-1]

    # Junta as palavras invertidas de volta em um string (sequência de caracteres)
    frase_invertida = ' '.join(palavras_invertidas)

    # Exibe os resultados
    print(f'\nA frase possui {numero_de_palavras} palavras')
    print(f'Frase invertida: {frase_invertida}')

processar_frase()