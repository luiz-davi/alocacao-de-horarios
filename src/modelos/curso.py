from modelos.enums.horarios import lista_horarios
from modelos.enums.dias import lista_dias
from tabulate import tabulate

class Curso:
    def __init__(self, nome, grade = None):
        self.nome = nome
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
                    if matriz[horario][dia] is None:
                        linha.append('-')
                    else:
                        linha.append(matriz[horario][dia].nome)
                    
                tabela.append(linha)

            print(tabulate(tabela, tablefmt='grid'))
            print()