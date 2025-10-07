class Calculadora: 
    def __init__(self):
        pass

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b
    
    def multiplicar(self, a, b):
        return a * b 
    
    def dividir(self, a, b):
        return a / b 
    
    def resto_divisao(self, a, b):
        return a % b

    def exponenciacao(self, a, b):
        return a ** b  
# Criação do Objeto

calc = Calculadora()
# Chamar os métodos e impressão dos resultados
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
resultado_soma = calc.somar(a, b)
resultado_subtracao = calc.subtrair(a, b)
resultado_multiplicar = calc.multiplicar(a, b)
resultado_dividir = calc.dividir(a, b)
resultado_restodivisao = calc.resto_divisao(a, b)
resultado_exponeciacao = calc.exponenciacao(a, b)

print(f"\nA soma {a} + {b} é: {resultado_soma:.2f}")
print(f"\nA subtração {a} - {b} é: {resultado_subtracao:.2f}")
print(f"\nA multiplicação {a} * {b} é: {resultado_multiplicar:.2f}")
print(f"\nA divisão {a} / {b} é: {resultado_dividir:.2f}")
print(f"\nO resto da divisão {a} % {b} é: {resultado_restodivisao:.2f}")
print(f"\nA exponenciação {a} ** {b} é: {resultado_exponeciacao:.2f}")