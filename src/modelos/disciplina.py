class Disciplina:

    def __init__(self, nome, quantidade_de_aulas, docentes=None):
        self.nome = nome
        self.quantidade_de_aulas = quantidade_de_aulas
        self.docentes = docentes if docentes is not None else []
