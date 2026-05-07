class PersonalTrainer():
    def __init__(self):
        self.alunos = []

    def faixa_etaria(self, idade):
        if idade < 17:
            return "Adolescente"
        elif (idade >= 18) and (idade < 60):
            return "Adulto"
        else:
            return "Idoso"
# crud

    def cadastrar_aluno(self):
        print("=-=-=--=-= Cadastrar Aluno =-=-=-=-=")

        nome = input("Nome do aluno ->")
        idade = float(input("Idade do aluno ->"))
        print("1 - Emagrecer")
        print("2 - Ganhar massa ")
        print("3 - Melhorar condicionamento")
        treino = int(input("Digite sua meta de treino do aluno->"))
        print("1 - Domingo")
        print("2 - Segunda")
        print("3 - Terça")
        print("4 - Quarta")
        print("5 - Quinta")
        print("6 - Sexta")
        print("7 - Sábado")
        entrada = input(
            "Dias disponíveis para treino (Coloque entre vírgulas)->")
        dias_disponiveis = [int(dia) for dia in entrada.split(",")]
        horas = float(
            input("Digite a quantidade de horas disponiveis por dia ->"))
        lesao = input("Possui lesão->")
        faixa = self.faixa_etaria(idade)
        aluno = {
            "nome": nome,
            "idade": idade,
            "faixa": faixa,
            "treino": treino,
            "dias_disponiveis": dias_disponiveis,
            "horas": horas,
            "lesao": lesao
        }

        self.alunos.append(aluno)
        print("=-=-=-=-= Aluno cadastrado com sucesso =-=-=-=-=")
# read

    def listar_alunos(self):
        print("=-=-=-=-= Listando Alunos =-=-=-=-=")
        if not self.alunos:
            print("=-=-=-= Nenhum Aluno Cadastrado =-=-=-=")
            return

        for i, aluno in enumerate(self.alunos):
            print("=-=" * 10)
            print(f"{i} - {aluno['nome']} |  {aluno['faixa']}")
            print("=-=" * 10)

        return True

# update
    def atualizar_alunos(self):
        if not self.listar_alunos():
            return

        indice = int(input("Digite o indice que deseja atualizar ->"))

        if indice < len(self.alunos):
            idade = int(input("Digite a nova idade ->"))
            print("1 - Emagrecer")
            print("2 - Ganhar massa ")
            print("3 - Melhorar condicionamento")
            faixa = self.faixa_etaria(idade)
            treino = int(input("Digite a nova meta de treino->"))
            print("1 - Domingo")
            print("2 - Segunda")
            print("3 - Terça")
            print("4 - Quarta")
            print("5 - Quinta")
            print("6 - Sexta")
            print("7 - Sábado")
            entrada = input(
                "Atualizar dias disponíveis para treino (Coloque entre vírgulas)->")
            dias_disponiveis = [int(dia) for dia in entrada.split(",")]
            horas = float(
                input("Nova quantidade de horas disponiveis por dia ->"))
            lesao = input("Possui lesão(atuallizar)->")

            self.alunos[indice]["idade"] = idade
            self.alunos[indice]["faixa"] = faixa
            self.alunos[indice]["treino"] = treino
            self.alunos[indice]["dias_disponiveis"] = dias_disponiveis
            self.alunos[indice]["horas"] = horas
            self.alunos[indice]["lesao"] = lesao
            print("=-=-=-=-=-=-=- Dados atualizados com sucesso=-=-=-=-=-=-=")
        else:
            print("Aluno não encontrado")
# delete

    def deletar_aluno(self):
        if not self.listar_alunos():
            return
        indice = int(input("Qual indice você deseja remover ->"))

        if indice < len(self.alunos):
            removido = self.alunos.pop(indice)
            print(
                f"=-=-=-=-=-=-= Aluno {removido['nome']} Removido =-=--=-=-=-=-=-=")
        else:
            print("Aluno não encontrado!")
# Gerar ficha de treino

    def gerar_treino(self):
        if not self.listar_alunos():
            return

        indice = int(input("Digite o indice do aluno ->"))

        if indice >= len(self.alunos):
            print("Aluno não encontrado!")
            return

        nome = self.alunos[indice]["nome"]
        faixa = self.alunos[indice]["faixa"]
        print(f"Treino para: {nome} | Faixa Etária: {faixa}")

        if faixa == "Adolescente":
            print("Treino Sugerido:")
            print("------------------")
            print(" - 15 min de corrida leve")
            print(" - 3x12 flexões")
            print(" - 3x15 agachamentos")
            print(" - Alongamento")
            print("------------------")
        elif faixa == "Adulto":
            print("Treino Sugerido:")
            print("------------------")
            print(" - 20 min cardio")
            print(" - 4x10 supino")
            print(" - 4x10 agachamentos")
            print(" - Exercicios leves com peso")
            print("------------------")
        else:
            print("Treino Sugerido:")
            print("------------------")
            print(" - Caminhada leve")
            print(" - Exercícios de mobilidade")
            print(" - Alongamento")
            print(" - Exercicios leves com peso")
            print("------------------")
# menu

    def menu(self):
        while True:
            print("===== UEMAFIT - SISTEMA DE TREINOS =====")
            print("1- Cadastrar um aluno")
            print("2- Listar alunos cadastrados")
            print("3- Atualizar dados")
            print("4- Remover um aluno")
            print("5- Gerar ficha de treino")
            print("6- Sair")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=")
            op = int(input("Digite uma das opções acima ->"))

            if op == 1:
                self.cadastrar_aluno()
            elif op == 2:
                self.listar_alunos()
            elif op == 3:
                self.atualizar_alunos()
            elif op == 4:
                self.deletar_aluno()
            elif op == 5:
                self.gerar_treino()
            elif op == 6:
                print("Saindo ...")
                break
            else:
                print("=-=-"*10)
                print("Selecione uma opção correta!")
                print("=-=-"*10)


personal = PersonalTrainer()
personal.menu()
