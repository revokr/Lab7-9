class Nota:
    def __init__(self, id_nota, Student, Disciplina, valoare):
        self.__id_nota = id_nota
        self.__Student = Student
        self.__Disciplina = Disciplina
        self.__valoare_nota = valoare

    def get_id_nota(self):
        return self.__id_nota

    def get_student_nota(self):
        return self.__Student

    def get_disciplina_nota(self):
        return self.__Disciplina

    def get_valoare_nota(self):
        return self.__valoare_nota