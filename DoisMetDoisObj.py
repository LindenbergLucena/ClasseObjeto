class Pessoa:

    # Classe que representa uma pessoa com nome e idade.
    
    def __init__(self, nome, idade): # construtor da classe pessoa para nome e idade.
       
        self.nome = nome
        self.idade = idade

    def apresentacao(self):
        # Método para apresentar a pessoa.
        
        # return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

    def aniversario(self):

        # Método para acrescentar 10 anos a idade da pessoa.
        
        self.idade += 10
        # return f"Que vergonha {self.nome}! Você está negando sua idade. Hoje você tem {self.idade} anos."
        print(f"{self.nome}, você está negando sua idade. Hoje você tem {self.idade} anos.")


# Criando dois objetos da classe Pessoa
pessoa1 = Pessoa("Pacatônio", 40)
pessoa2 = Pessoa("Ambrozina", 36)

# Usando os métodos nos objetos criados
print(pessoa1.apresentacao())  # Saída: Olá, meu nome é Pacatônio e eu tenho 40 anos.
print(pessoa2.apresentacao())  # Saída: Olá, meu nome é Ambrozina e eu tenho 36 anos.

print(pessoa1.aniversario())  # Saída: Pacatônio, você está negando sua idade. Hoje você tem 50 anos.
print(pessoa2.aniversario())  # Saída: Ambrozina, você está negando sua idade. Hoje você tem 46 anos.