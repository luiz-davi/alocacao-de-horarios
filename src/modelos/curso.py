from modelos.enums.horarios import lista_horarios
from modelos.enums.dias import lista_dias
from tabulate import tabulate

class Curso:
    def __init__(self, nome, quantidade_periodos, grade = None):
        self.nome = nome
        self.quantidade_periodos = quantidade_periodos
        self.grade = grade

    def imprimir_grade(grade):
        quantidade_horarios = len(lista_horarios)

        # Percorre todos os períodos do curso
        for periodo, matriz in enumerate(grade, start=1):
            # Adiciona o cabeçalho com número do período e dias letivos da semana
            tabela = [[f"Periodo {periodo}"] + lista_dias]

            # Percorre todas as linhas (horários)
            for horario in range(quantidade_horarios):
                # Adiciona o horário na esquerda, abaixo do número do período
                linha = [lista_horarios[horario]]

                # Percorre todas as colunas (dias)
                for dia in range(len(matriz[horario])):
                    linha.append(matriz[horario][dia])
                tabela.append(linha)

            print(tabulate(tabela, tablefmt='grid'))
            print()