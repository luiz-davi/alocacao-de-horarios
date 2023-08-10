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
import time

start_time = time.time()

DOCENTES, DISCIPLINAS = professores_disciplinas();
TOTAL_GERACOES = 0

def menos_apto(populacao):
  infos = { 'aptidao': MELHOR_APTIDAO, 'grade': [], 'posicao': None }

  for index, grade in enumerate(populacao):
    aptidao = calcular_aptidao(grade)
    if aptidao < calcular_aptidao(infos['grade']):
      infos['aptidao'] = aptidao
      infos['grade'] = grade
      infos['posicao'] = index
  
  return infos

def mais_apto(populacao):
  infos = { 'aptidao': -99999999, 'grade': [], 'posicao': None }

  for index, grade in enumerate(populacao):
    aptidao = calcular_aptidao(grade)
    if aptidao > infos['aptidao']:
      infos['aptidao'] = aptidao
      infos['grade'] = grade
      infos['posicao'] = index
  
  return infos

def mutacao(grade):
  periodo_mutado = random.randint(1, QUANT_DE_PERIODOS)

  novo_periodo = [[None for _ in range(QUANT_DE_DIAS)] for _ in range(QUANT_DE_HORARIOS)]

  preencher_horario(periodo_mutado, novo_periodo, DISCIPLINAS)

  grade[periodo_mutado - 1] = novo_periodo


"""
  para cada período escolhe aleatoriamente umas das grades para herdar as disciplinas
  ao final aplica as mutações
"""
def crossover(grade1, grade2):
  grade_filha = []

  for index in range(QUANT_DE_PERIODOS):
    grade_pai = random.choice([grade1, grade2])
    grade_filha.append(grade_pai[index])
  
  for _ in range(QUANT_MUTACOES):
    mutacao(grade_filha)
  
  return grade_filha


def calcular_aptidao(grade):
    aptidao = MELHOR_APTIDAO
    
    # Criar um dicionário para armazenar os horários de cada docente
    horarios_docentes = { docente.nome: set() for docente in DOCENTES }
    
    # Percorrer a grade de horários verificando se há choques
    for periodo in grade:
        for dia in range(QUANT_DE_DIAS):
            for horario in range(QUANT_DE_HORARIOS):
                disciplina = periodo[horario][dia]
                if disciplina:
                    for docente in disciplina.docentes:
                        if (dia, horario) in horarios_docentes[docente.nome]:
                            # Choque de horário, remover pontuação
                            aptidao -= PONTUACAO_CHOQUE
                            #print(f"Choque no dia {LISTA_DIAS[dia]} às {LISTA_HORARIOS[horario]} do professor {docente.nome}")
                            break
                        else:
                            horarios_docentes[docente.nome].add((dia, horario))
                            dia_bom = True
                            for dia_nao_lecionavel in docente.dias_sem_lecionar:
                               if dia_nao_lecionavel == dia:
                                  aptidao -= PONTUACAO_DIA_NAO_LECIONAVEL
                                  dia_bom = False
                                  #print(f"Docente {docente.nome} lecionando no dia {LISTA_DIAS[dia]} às {LISTA_HORARIOS[horario]}")
                                  break
                            if dia_bom:
                               aptidao += 2

    return aptidao

"""
  Troca as grades mais aptas pelas menos aptas
  *menos_apto return ex.: { 'aptidao': -3000, 'grade': [...], 'posicao': 0 }
"""
def thanos(novas_grades, populacao):
  for nova_grade in novas_grades:
      grade_ruim = menos_apto(populacao)
      nova_aptidao = calcular_aptidao(nova_grade)
      if nova_aptidao > grade_ruim['aptidao']:
          populacao[grade_ruim['posicao']] = nova_grade


populacao = criar_populacao_inicial(DISCIPLINAS)

esforcado = mais_apto(populacao)
melhor = { 
  'aptidao': esforcado['aptidao'] ,
  'grade': esforcado['grade'], 
  'posicao': esforcado['posicao'],
  'geracao': 0
}

while melhor['geracao'] < QUANT_GERACOES_SEM_MELHORIA:
  novas_grades = []
  for i in range(0, len(populacao), 2):
      grade1 = populacao[i]
      grade2 = populacao[i+1]

      novas_grades.append(crossover(grade1, grade2))

  TOTAL_GERACOES += 1
  melhor['geracao'] += 1
  thanos(novas_grades, populacao)

  esforcado = mais_apto(populacao)
  if esforcado['aptidao'] > melhor['aptidao']:
    melhor['aptidao'] = esforcado['aptidao']
    melhor['grade'] = esforcado['grade']
    melhor['posicao'] = esforcado['posicao']
    melhor['geracao'] = 0


if(melhor['aptidao'] == MELHOR_APTIDAO):
   Curso.imprimir_grade(melhor['grade'])
   print("Encontrou a grade perfeita")
elif(melhor['aptidao'] <= (PONTUACAO_CHOQUE * -1)):
  print("Não encontrou grade sem choque de horários")
else:
   print("Melhor grade:")
   Curso.imprimir_grade(melhor['grade'])

print(f'Total de gerações: {TOTAL_GERACOES}')


end_time = time.time()
execution_time = end_time - start_time

minutos = int(execution_time // 60)
segundos = int(execution_time % 60)
print(f"Tempo de execução: {minutos} minuto(s) e {segundos} segundo(s)")