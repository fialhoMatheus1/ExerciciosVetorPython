from Model import Model

class Control:
    def __init__(self):
        self.model = Model()
        self.opcao = -1

    def menu(self):
        print("\n\nEscolha uma das opções abaixo:" +
              "\n0. Sair" +
              "\n1. Exercício 1")
        self.opcao = int(input())

    def operacao(self):
        while self.opcao != 0:
            self.menu()
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                self.model.exercicio01()