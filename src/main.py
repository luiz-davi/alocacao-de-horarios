import os
import sys
import random

# Obter o caminho absoluto da pasta 'factory'
current_dir = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(current_dir, '..')
sys.path.append(main_path)

from modelos.curso import Curso
from factory.oferta_disciplinas import professores_disciplinas

# retornar um array dos docentes que irão lecionar a disciplina especificada
def filtrar_docentes(docentes, disciplina):
  return [doc for doc in docentes if disciplina.nome in doc.conjunto_de_disciplinas]

# aplicar lógica de validações apartir dos docentes da disciplinas
# aplicadas as validações, retornar dados para tomada de decisões
def possuem_aulas_concentradas(docentes):
    boolean = [doc.aulas_concentradas for doc in docentes]

    return True

docentes1, disciplinas_por_periodo = professores_disciplinas();

# Lista de matrizes de horários vazia para cada período
periodos = []  # aqui serão adicionados os períodos

# Função para preencher uma matriz de horários com as disciplinas do período
def preencher_horario(periodo, matriz_horario):
    horarios_disponiveis = 10  # Cada período tem 10 horários disponíveis
    disciplinas_do_periodo = [disc for disc in disciplinas_por_periodo if disc.periodo == periodo]
    random.shuffle(disciplinas_do_periodo)  # Embaralha as disciplinas do período
    
    for disciplina in disciplinas_do_periodo:
        docentes = filtrar_docentes(docentes1, disciplina)
        aulas_restantes = disciplina.quantidade_de_aulas
        for horario in range(2):
            for dia in range(5):
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
    matriz_horario = [['-' for _ in range(5)] for _ in range(2)]  # Cria matriz de 2x5 com '-'
    preencher_horario(periodo, matriz_horario)
    periodos.append(matriz_horario)  # Atualiza diretamente a matriz de horário do período

Curso.imprimir_grade(periodos)