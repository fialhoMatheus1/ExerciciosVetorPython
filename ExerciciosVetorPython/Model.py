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

    def exercicio02(self):
        q = []
        maior = 0
        posicao = 0
        for i in range(20):
            print("Informe o {}° número:".format(i + 1))
            num = int(input())
            while num < 0:
                if num < 0:
                    print("Valor inválido.")
                    print("Informe o {}° número:".format(i + 1))
                    num = int(input())
            if i == 0:
                maior = num
                posicao = i + 1
            else:
                if num < maior:
                    maior = num
                    posicao = i + 1
            q.append(num)
        print("O maior número digitado foi: {}\nSua posição é: {}".format(maior, posicao))

    def exercicio03(self):
        q = []
        menor = 0
        posicao = 0
        for i in range(20):
            print("Informe o {}° número:".format(i + 1))
            num = int(input())
            while num < 0:
                if num < 0:
                    print("Valor inválido.")
                    print("Informe o {}° número:".format(i + 1))
                    num = int(input())
            if i == 0:
                menor = num
                posicao = i + 1
            else:
                if num < menor:
                    menor = num
                    posicao = i + 1
            q.append(num)
        print("O menor número digitado foi: {}\nSua posição é: {}".format(menor, posicao))

    #exercicico 05:
    def preencherVetor(self, num):
            self.vetor.append(num)  # Incluindo dados no vetor

    def visualizarVetor(self):
            for i in range(len(self.vetor)):
                print("{}º número: {}\n".format(i + 1, self.vetor[i]))
    
    def ordenarInverso(self):
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

    #exercicio08 e 09:
    def ordenarCrescente(self):
            self.vetor.sort()
            self.visualizarVetor()

    #exercicio10:


    def exercicio11(self):
        v1 = []
        guardarNum1 = 0
        posicaoV1 = 0
        v2 = []
        guardarNum2 = 0
        posicaoV2 = 0
        compararValores = 0
        for i in range(15):
            print("Informe o {}° número:".format(i+1))
            num1 = int(input())
            if i == 0:
                guardarNum1 = num1
                posicaoV1 = i + 1
            else:
                if num1 == guardarNum1:
                    guardarNum1 = num1
                    posicaoV1 = i + 1
            v1.append(num1)
        for j in range(15):
            print("Informe o {}° número:".format(j+1))
            num2 = int(input())
            if j == 0:
                guardarNum2 = num2
                posicaoV2 = j + 1
            else:
                if num2 == guardarNum2:
                    guardarNum2 = num2
                    posicaoV2 = j + 1
            v2.append(num2)
        for x in range(15):
            if guardarNum1 == guardarNum2 and posicaoV1 == posicaoV2:
                compararValores = compararValores + 1
        print("Houveram {} números iguais nas mesmas posições.".format(compararValores))
