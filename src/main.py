import os
import sys
import random

# Obter o caminho absoluto da pasta 'factory'
current_dir = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(current_dir, '..')
sys.path.append(main_path)

from factory.oferta_disciplinas import professores_disciplinas
from factory.populacao_inicial import preencher_horario, criar_populacao_inicial
from modelos.curso import Curso
from constantes import *

DOCENTES, DISCIPLINAS = professores_disciplinas();


# gera uma grade com base em duas outras grades
def mutacao(grade):
  periodo_mutado = random.randint(1, QUANT_DE_PERIODOS)

  novo_periodo = [[None for _ in range(QUANT_DE_DIAS)] for _ in range(QUANT_DE_HORARIOS)]

  preencher_horario(periodo_mutado, novo_periodo, DISCIPLINAS)

  grade[periodo_mutado - 1] = novo_periodo


# para cada período escolhe aleatoriamente umas das grades para herdar as disciplinas
# ao final aplica as mutações
def crossover(grade1, grade2):
  grade_filha = []

  for index in range(QUANT_DE_PERIODOS):
    grade_pai = random.choice([grade1, grade2])
    grade_filha.append(grade_pai[index])
  
  for _ in range(QUANT_MUTACOES):
    mutacao(grade_filha)
  
  return grade_filha


populacao_inicial = criar_populacao_inicial(DISCIPLINAS)

grade = crossover(populacao_inicial[0], populacao_inicial[1])

Curso.imprimir_grade(grade)
