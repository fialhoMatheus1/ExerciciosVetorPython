class Model:
    def __init__(self):
        self.vetor = []

    def exercicio01(self):
        nota = []
        media = 0
        soma = 0
        maior = 0
        for i in range(20):
            print("Informe a nota do {}° aluno:".format(i+1))
            num = float(input())

            while num < 0 or num > 10:
                if num < 0 or num > 10:
                    print("Valor inválido.")
                    print("Informe a nota do {}° aluno:".format(i + 1))
                    num = float(input())

            nota.append(num)
            soma = soma + num
        media = soma / 20
        for i in range(20):
            if nota[i] > media:
                maior = maior + 1
        print("A média da turma é: {}\nHouveram {} notas acima da média.".format(media, maior))

    def exercicio03(self):
        q = []
        menor = 0
        for i in range(3):
            print("Informe o {}° número:".format(i+1))
            num = int(input())
            while num < 0:
                if num < 0:
                    print("Valor inválido.")
                    print("Informe o {}° número:".format(i+1))
                    num = int(input())
            if i == 0:
                        menor = num
            else:
                if num < menor:
                            menor = num
            q.append(num)
        print("A menor valor de Q é: {}\nSua posição é: (nao sei >:( ))".format(menor))

    #exercicico 05:
    def preencherVetor(self, num):
            self.vetor.append(num)  # Incluindo dados no vetor

    def visualizarVetor(self):
            for i in range(len(self.vetor)):
                print("{}º número: {}\n".format(i + 1, self.vetor[i]))
    
    def ordenarDecrescente(self):
            self.vetor.sort(reverse=True)
            self.visualizarVetor()

    def exercicio07(self):
        vetorGrau = []
        soma = 0
        menor = 0
        maior = 0
        media = 0
        acimaMedia = 0
        for i in range(365):
            print("Informe uma temperatura:")
            grau = int(input())
            
            if i == 0:
                if grau < 0:
                    menor = grau
                if grau >= 0:
                    maior = grau
            else:
                if grau < menor:
                    menor = grau
                if grau > maior:
                    maior = grau

            vetorGrau.append(grau)
            soma = soma + grau
        media = soma / 365
        for i in range(365):
            if vetorGrau[i] > media:
                acimaMedia = acimaMedia + 1
        print("Menor temperatura do ano: {}°\nMaior temperatura do ano: {}°\nMédia anual: {}°\nDias com temperatura acima da média: {} dias".format(menor, maior, media, acimaMedia))

    #exercicio 9:
    def ordenarCrescente(self):
            self.vetor.sort()
            self.visualizarVetor()
