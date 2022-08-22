class Model:
    def __init__(self):
        self.vetor = []

    #metodo para receber os dados dos exercicios

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
        menor =0
        for i in range(5):
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
        #operações com vetor:
        print("A menor valor de Q é: {}\nSua posição é: {}".format(menor))
