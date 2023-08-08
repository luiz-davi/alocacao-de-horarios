import os
import sys
import random

# Obter o caminho absoluto da pasta 'factory'
current_dir = os.path.dirname(os.path.abspath(__file__))
factory_path = os.path.join(current_dir, '..')
sys.path.append(factory_path)

from modelos.curso import Curso
from modelos.enums.horarios import lista_horarios
from modelos.enums.dias import lista_dias
import oferta_disciplinas

docentes, disciplinas_por_periodo = oferta_disciplinas.exec();

periodos = []
quantidade_dias = len(lista_dias)
quantidade_horarios = len(lista_horarios)

# Função para preencher uma matriz de horários com as disciplinas do período
def preencher_horario(periodo, matriz_horario):
    horarios_disponiveis = 10  # Cada período tem 10 horários disponíveis
    disciplinas_do_periodo = [disc for disc in disciplinas_por_periodo if disc.periodo == periodo]
    random.shuffle(disciplinas_do_periodo)  # Embaralha as disciplinas do período
    for disciplina in disciplinas_do_periodo:
        aulas_restantes = disciplina.quantidade_de_aulas
        for horario in range(quantidade_horarios):
            for dia in range(quantidade_dias):
                if aulas_restantes > 0 and matriz_horario[horario][dia] == '-':
                    matriz_horario[horario][dia] = disciplina.nome
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
    matriz_horario = [['-' for _ in range(quantidade_dias)] for _ in range(quantidade_horarios)]  # Cria matriz de 2x5 com '-'
    preencher_horario(periodo, matriz_horario)
    periodos.append(matriz_horario)  # Atualiza diretamente a matriz de horário do período

Curso.imprimir_grade(periodos)