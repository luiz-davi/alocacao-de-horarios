class Disciplina:

    def __init__(self, nome, quantidade_de_aulas, periodo, docentes=None):
        self.nome = nome
        self.quantidade_de_aulas = quantidade_de_aulas
        self.periodo = periodo
        self.docentes = docentes if docentes is not None else []
