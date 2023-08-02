from modelos.disciplina import Disciplina
import os
import sys

# Obter o caminho absoluto da pasta 'factory'
current_dir = os.path.dirname(os.path.abspath(__file__))
factory_path = os.path.join(current_dir, '..')
sys.path.append(factory_path)


def retornar_professores(nome):
    infos_professor = {
        'marcius': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'calculo 1',
            ],
        },
        'luis': {
            'dias_sem_lecionar': [3, 4],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'introducao a programacao',
                'optativa 3',
            ],
        },
        'ryan': {
            'dias_sem_lecionar': [0, 1],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'inteligencia artificial',
                'optativa 4',
            ],
        },
        'gersonilo': {
            'dias_sem_lecionar': [0, 1],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'logica matematica',
                'algebra linear',
                'matematica discreta',
            ],
        },
        'igor': {
            'dias_sem_lecionar': [3, 4],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'poo',
                'aed 2',
            ],
        },
        'sansuke': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'calculo 2',
            ],
        },
        'wellington': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'fisica'
            ],
        },
        'romero': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'probabilidade e estatistica'
            ],
        },
        'helder': {
            'dias_sem_lecionar': [3, 4],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'sistemas digitais',
                'arquitetura de computadores',
            ],
        },
        'niege': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'metodologia cientifica'
            ],
        },
        'diana': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'ingles'
            ],
        },
        'r. andrade': {
            'dias_sem_lecionar': [2, 3, 4],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'engenharia de software',
                'interacao humano-computador',
            ],
        },
        'priscilla': {
            'dias_sem_lecionar': [2, 3],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'aed 1',
                'optativa 2',
            ],
        },
        'alvaro': {
            'dias_sem_lecionar': [2, 3],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'paradigmas de linguagens de programacao',
                'optativa 5',
            ],
        },
        'maria': {
            'dias_sem_lecionar': [2, 3, 4],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'teoria da computacao',
                'compiladores',
            ],

        },
        'kadna': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'redes de computadores',
                'optativa 1'
                'estagio supervisionado obrigatorio',
            ],

        },
        'assuero': {
            'dias_sem_lecionar': [2, 3, 4],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'sistemas de informacao',
                'empreendedorismo',
            ],

        },
        'tiago': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'reconhecimento de padroes'
            ],

        },
        'sergio': {
            'dias_sem_lecionar': [0, 1, 2],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'introducao a programacao',
                'sistemas operacionais',
                'computadores e sociedade',
            ],

        },
        'icaro': {
            'dias_sem_lecionar': [0, 1],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'computacao grafica',
                'optativa 6'
            ],

        },
        'jean': {
            'dias_sem_lecionar': [0, 1, 2],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'sistemas distribuidos',
                'optativa 7',
            ],
        },
        'r. gusmao': {
            'dias_sem_lecionar': [0, 1],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'projeto de desenvolvimento',
                'estagio supervisionado obrigatorio',
            ],

        },
        'dimas': {
            'dias_sem_lecionar': [0, 1, 4],
            'aulas_concentradas': True,
            'conjunto_de_disciplinas': [
                'paradigmas de linguagens de programacao',
                'banco de dados',
            ],
        },
        'thais': {
            'dias_sem_lecionar': [],
            'aulas_concentradas': False,
            'conjunto_de_disciplinas': [
                'tcc',
            ],
        },
    }

    return infos_professor[nome]


def retornar_disciplinas():
    return [
        Disciplina('calculo 1', 2),
        Disciplina('introducao a programacao', 3),
        Disciplina('logica matematica', 2),
        Disciplina('geometria analitica', 2),
        Disciplina('introducao a computacao', 1),

        Disciplina('poo', 2),
        Disciplina('calculo 2', 2),
        Disciplina('algebra linear', 2),
        Disciplina('fisica', 2),
        Disciplina('aed 1', 2),

        Disciplina('probabilidade e estatistica', 2),
        Disciplina('sistemas digitais', 2),
        Disciplina('aed 2', 2),
        Disciplina('matematica discreta', 2),
        Disciplina('metodologia cientifica', 2),
        Disciplina('ingles', 1),

        Disciplina('arquitetura de computadores', 2),
        Disciplina('engenharia de software', 2),
        Disciplina('paradigmas de linguagens de programacao', 2),
        Disciplina('banco de dados', 2),
        Disciplina('projeto e analise de algoritmos', 2),

        Disciplina('teoria da computacao', 2),
        Disciplina('sistemas de informacao', 2),
        Disciplina('redes de computadores', 2),
        Disciplina('sistemas operacionais', 2),
        Disciplina('inteligencia artificial', 2),

        Disciplina('empreendedorismo', 2),
        Disciplina('compiladores', 2),
        Disciplina('reconhecimento de padroes', 2),
        Disciplina('sistemas distribuidos', 2),
        Disciplina('computacao grafica', 2),

        Disciplina('interacao humano-computador', 2),
        Disciplina('projeto de desenvolvimento', 3),
        Disciplina('computadores e sociedade', 1),

        Disciplina('optativa 1', 2),
        Disciplina('optativa 2', 2),
        Disciplina('optativa 3', 2),
        Disciplina('optativa 4', 2),
        Disciplina('optativa 5', 2),
        Disciplina('optativa 6', 2),
        Disciplina('optativa 7', 2),

        Disciplina('estagio supervisionado obrigatorio', 1),
        Disciplina('tcc', 1),
    ]
