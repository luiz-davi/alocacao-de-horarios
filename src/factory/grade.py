from modelos.enums.professores import professores
from modelos.enums.disciplinas import disciplinas
import infos
from modelos.docente import Docente

def criar_professores():
    docentes = []
    for nome in professores:
        infos_prof = infos.professores(nome)
        professor = Docente(nome, infos_prof['dias_sem_lecionar'],
                            infos_prof['aulas_concentradas'],
                            infos_prof['conjunto_de_disciplinas'])
        docentes.append(professor)

    return docentes


def criar_disciplinas():
    docentes = criar_professores()
    cadeiras = infos.disciplinas()

    for docente in docentes:
        for disciplina in docente.conjunto_de_disciplinas:
            for cadeira in cadeiras:
                if disciplina == cadeira.nome:
                    cadeira.docente.append(docente)

    return docentes, cadeiras


def exec():
    docentes, cadeiras = criar_disciplinas()
    return docentes, cadeiras
