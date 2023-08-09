import os
import sys
import random


# Obter o caminho absoluto da pasta 'factory'
current_dir = os.path.dirname(os.path.abspath(__file__))
populacao_inicial_path = os.path.join(current_dir, '..')
sys.path.append(populacao_inicial_path)

from constantes import *

# Função para preencher uma matriz de horários com as disciplinas do período
def preencher_horario(periodo, matriz_horario, disciplinas):
    horarios_disponiveis = QUANT_HORARIOS_DISPO  # Cada período tem 10 horários disponíveis
    disciplinas_do_periodo = [disc for disc in disciplinas if disc.periodo == periodo]
    random.shuffle(disciplinas_do_periodo)  # Embaralha as disciplinas do período

    for disciplina in disciplinas_do_periodo:
        aulas_restantes = disciplina.quantidade_de_aulas
        for horario in range(QUANT_DE_HORARIOS):
            for dia in range(QUANT_DE_DIAS):
                if aulas_restantes > 0 and matriz_horario[horario][dia] == None:
                    matriz_horario[horario][dia] = disciplina
                    aulas_restantes -= 1
                    horarios_disponiveis -= 1
                    if aulas_restantes == 0:
                        break
            if aulas_restantes == 0:
                break
        if horarios_disponiveis == 0:
            break


def criar_populacao_inicial(disciplinas):
    populacao = []

    for _ in range(QUANT_DA_POPULACAO_INICIAL):
        periodos = []

        # Preenche as matrizes de horários para cada período
        for periodo in range(1, QUANT_DE_PERIODOS + 1):
            # inicializa o período com valores nulos
            matriz_horario = [[None for _ in range(QUANT_DE_DIAS)] for _ in range(QUANT_DE_HORARIOS)]
            
            preencher_horario(periodo, matriz_horario, disciplinas)
            
            # Atualiza diretamente a matriz de horário do período
            periodos.append(matriz_horario)

        populacao.append(periodos)
    
    return populacao

