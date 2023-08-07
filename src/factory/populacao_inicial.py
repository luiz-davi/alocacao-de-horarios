import os
import sys
import random

# Obter o caminho absoluto da pasta 'factory'
current_dir = os.path.dirname(os.path.abspath(__file__))
factory_path = os.path.join(current_dir, '..')
sys.path.append(factory_path)

from modelos.curso import Curso
from infos import retornar_disciplinas

disciplinas_por_periodo = retornar_disciplinas()

# Cria uma lista de matrizes de horários vazia para cada período
periodos = [[] for _ in range(9)]  # 9 períodos (de 1 a 9)

# Função para preencher uma matriz de horários com as disciplinas do período
def preencher_horario(periodo, matriz_horario):
    horarios_disponiveis = 10  # Cada período tem 10 horários disponíveis
    disciplinas_do_periodo = [disc for disc in disciplinas_por_periodo if disc.periodo == periodo]
    random.shuffle(disciplinas_do_periodo)  # Embaralha as disciplinas do período
    for disciplina in disciplinas_do_periodo:
        aulas_restantes = disciplina.quantidade_de_aulas
        for i in range(2):
            for j in range(5):
                if aulas_restantes > 0 and matriz_horario[i][j] == '-':
                    matriz_horario[i][j] = disciplina.nome
                    aulas_restantes -= 1
                    horarios_disponiveis -= 1
                    if aulas_restantes == 0:
                        break
            if aulas_restantes == 0:
                break
        if horarios_disponiveis == 0:
            break

# Preenche as matrizes de horários para cada período
for periodo in range(1, 10):
    matriz_horario = [['-' for _ in range(5)] for _ in range(2)]  # Cria matriz de 2x5 com '-'
    preencher_horario(periodo, matriz_horario)
    periodos[periodo - 1] = matriz_horario  # Atualiza diretamente a matriz de horário do período

Curso.imprimir_grade(periodos)