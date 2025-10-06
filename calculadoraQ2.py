class Calculadora: 
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b
# Criação do Objeto

calc = Calculadora()
# Chamar os métodos e impressão dos resultados
resultado_soma = calc.somar(15, 7)
resultado_subtracao = calc.subtrair(25, 8)

print(f"A soma 15 + 7 é: {resultado_soma}")
print(f"A subtração 25 - 8 é: {resultado_subtracao}")