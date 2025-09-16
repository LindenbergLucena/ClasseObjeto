def classificar_numero():
    print('Digite um número. O programa será encerrado quando for digitado ZERO.')

    while = True
        try: # Tente até
            # solicita a entrada do usuário
            numero = float(input('Digite um número: '))

            # Usando estruturas de decisão para classificar o número:
            if numero > 0:
                print(f'\nO número {numero} é positivo')

            elif numero < 0:
                print(f'\nO número {numero} é negativo')

            else:
                print(f'Você digitou ZERO. O programa será encerrado.')

        except ValueError:
            print('Entrada inválida. Por favor digite um número válido.')
            
    classificar_numero()
            