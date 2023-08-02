from factory.infos import *
from modelos.enums.professores import professores
from modelos.docente import Docente
import os
import sys

# Obter o caminho absoluto da pasta 'factory'
current_dir = os.path.dirname(os.path.abspath(__file__))
factory_path = os.path.join(current_dir, '..')
sys.path.append(factory_path)


def criar_professores():
    docentes = []
    for nome in professores:
        infos_prof = retornar_professores(nome)
        professor = Docente(nome, infos_prof['dias_sem_lecionar'],
                            infos_prof['aulas_concentradas'],
                            infos_prof['conjunto_de_disciplinas'])
        docentes.append(professor)

    return docentes


def criar_disciplinas():
    docentes = criar_professores()
    cadeiras = retornar_disciplinas()

    for docente in docentes:
        for disciplina in docente.conjunto_de_disciplinas:
            for cadeira in cadeiras:
                if disciplina == cadeira.nome:
                    cadeira.docentes.append(docente)

    return docentes, cadeiras


def exec():
    docentes, cadeiras = criar_disciplinas()
    return docentes, cadeiras
