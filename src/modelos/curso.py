class Curso:
    def __init__(self, periodos):
        self.periodos = periodos
        self.grade = {}

        horarios = [[0 for coluna in range(2)] for dia in range(5)]
        for index in range(len(periodos)):
            self.grade[index + 1] = horarios
