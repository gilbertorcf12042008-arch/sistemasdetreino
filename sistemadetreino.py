class PersonalTrainer():
    def __init__(self):
       self.alunos = []

    def cadastrar_aluno(self):
        print("=-=-=--=-= Cadastrar Aluno =-=-=-=-=")

        nome = input("Digite o seu nome ->")
        idade = float(input("Digite sua idade ->"))
        treino = float(input("Digite sua meta de treino->"))
        print("1 - Emagrecer")
        print("2 - Ganhar massa ")
        print("3 - Melhorar condicionamento")
        dias = input("Dias disponíveis para treino->")
        print("1 - Domingo")
        print("2 - Segunda")
        print("3 - Terça")
        print("4 - Quarta")
        print("5 - Quinta")
        print("6 - Sexta")
        print("7 - Sábado")