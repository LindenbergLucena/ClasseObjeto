class Livro:
    # Representa um livro com título, autor e status.
    def __init__(self, titulo, autor):
        # O construtor inicializa os atributos do objeto.
        self.titulo = titulo
        self.autor = autor
        self.lido = False

    def marcar_como_lido(self):
        self.lido = True
              
    def exibir_status(self):
        # status = "Foi lido" if self.lido else "não foi lido"
        if self.lido:
                status = "Já foi lido"
        else:
                status = "Não foi lido"
        # return f"O livro {self.titulo} de {self.autor}, {status}"
        print(f"O livro {self.titulo} de {self.autor}, {status}")

# --- PRÁTICA ---
livro1 = Livro("A Arte da Guerra", "Sun Tzu") #objeto1 livro1
livro2 = Livro("O Alquimista", "Paulo Coelho") #objeto2 livro2

print("--- Livros Criados ---")

livro1.marcar_como_lido()
livro1.exibir_status()
livro2.exibir_status()

