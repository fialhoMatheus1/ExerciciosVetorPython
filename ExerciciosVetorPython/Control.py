from Model import Model

class Control:
    def __init__(self):
        self.model = Model()
        self.opcao = -1

    def menu(self):
        print("\n\nEscolha uma das opções abaixo:" +
              "\n0. Sair" +
              "\n1. Exercício 1" +
              "\n2. Exercício 2" +
              "\n3. Exercício 3" +
              "\n5. Exercício 5" +
              "\n7. Exercício 7" +
              "\n8. Exercício 8" +
              "\n9. Exercício 9" +
              "\n10. Exercício 10" +
              "\n11. Exercício 11")
        self.opcao = int(input())

    def operacao(self):
        while self.opcao != 0:
            self.menu()
            if self.opcao == 0:
                print("Obrigado!")
            elif self.opcao == 1:
                self.model.exercicio01()
            elif self.opcao == 2:
                self.model.exercicio02()
            elif self.opcao == 3:
                self.model.exercicio03()
            elif self.opcao == 5:
                i = 0
                for i in range(20):
                    print("Informe o {}º número: ".format(i + 1))
                    self.model.preencherVetor(int(input()))
                self.model.ordenarInverso()
            elif self.opcao == 7:
                self.model.exercicio07()
            elif self.opcao == 8:
                i = 0
                for i in range(20):
                    print("Informe um número:".format(i+1))
                    self.model.preencherVetor(int(input()))
                print("Números em ordem crescente:")
                self.model.ordenarCrescente()
            elif self.opcao == 9:
                i = 0
                for i in range(10):
                    print("Informe um número:".format(i+1))
                    self.model.preencherVetor(int(input()))
                print("Números em ordem crescente:")
                self.model.ordenarCrescente()
                for i in range(1):
                    print("Informe um último valor para ser incluído corretamente na ordem:")
                    self.model.preencherVetor(int(input()))
                print("Lista atualizada:")
                self.model.ordenarCrescente()
            #está incompleto
            elif self.opcao == 10:
                i = 0
                for i in range(5):
                    print("Informe um número:".format(i+1))
                    self.model.preencherVetor(int(input()))
                print("Números digitados:")
                self.model.visualizarVetor()
            elif self.opcao == 11:
                self.model.exercicio11()
            elif self.opcao == 13:
                pass

            else:
                print("Opcão inválida!")
