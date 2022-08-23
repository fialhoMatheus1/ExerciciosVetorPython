from Model import Model

class Control:
    def __init__(self):
        self.model = Model()
        self.opcao = -1

    def menu(self):
        print("\n\nEscolha uma das opções abaixo:" +
              "\n0. Sair" +
              "\n1. Exercício 1" +
              "\n3. Exercício 3" +
              "\n5. Exercício 5" +
              "\n6. Exercício 7" +
              "\n9. Exercício 9")
        self.opcao = int(input())

    def operacao(self):
        while self.opcao != 0:
            self.menu()
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                self.model.exercicio01()
            elif self.opcao == 3:
                self.model.exercicio03()
            elif self.opcao == 5:
                i = 0
                for i in range(20):
                    print("Informe o {}º número: ".format(i + 1))
                    self.model.preencherVetor(int(input()))
                self.model.ordenarDecrescente()
            elif self.opcao == 7:
                self.model.exercicio07()
            elif self.opcao == 9:
                i = 0
                for i in range(10):
                    print("Informe o {}º número: ".format(i + 1))
                    self.model.preencherVetor(int(input()))
                self.model.ordenarCrescente()
                print("\nInsira um valor:")
                valor = int(input())
            elif self.opcao == 10:
                self.model.teste()
            else:
                print("Opcão inválida!")

