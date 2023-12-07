class disciplina:
    def __init__(self, id_disciplina, nume_disciplina, profesor):
        self.__id_disciplina = id_disciplina
        self.__nume_disciplina = nume_disciplina
        self.__profesor = profesor

    def get_id_dis(self):
        return self.__id_disciplina

    def get_nume_dis(self):
        return self.__nume_disciplina

    def get_profesor(self):
        return self.__profesor