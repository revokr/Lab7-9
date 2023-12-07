from Exceptii.RepoError import RepoError
from domain.note import Nota
class repo_student:
    def __init__(self):
        self.__lista = {}

    def __len__(self):
        return len(self.__lista)

    def is_empty(self):
        return len(self.__lista) == 0


    def adauga_std(self, Student):
        if Student.get_id_student() in self.__lista:
            raise Exception("Student existent!!!")
        self.__lista[Student.get_id_student()] = Student


    def sterge_std(self, id_student):
        if id_student not in self.__lista:
            raise RepoError("Student inexistent!!!")
        del self.__lista[id_student]

    def cauta_student(self, id_student):
        if id_student not in self.__lista:
            raise RepoError("Student inexistent!!!")
        return self.__lista[id_student]

    def modifica_student(self, Student):
        id_student = Student.get_id_student()
        if id_student not in self.__lista:
            raise RepoError("Student inexistent!!!")
        self.__lista[id_student] = Student


    def get_all(self):
        return [self.__lista[id_student] for id_student in self.__lista]




class repo_discipline:
    def __init__(self):
        self.__lista_discipline = {}

    def __len__(self):
        return len(self.__lista_discipline)

    def is_empty(self):
        return len(self.__lista_discipline) == 0


    def adauga_dis(self, Disciplina):
        if Disciplina.get_id_dis() in self.__lista_discipline:
            raise Exception("Disciplina existenta!!!")
        self.__lista_discipline[Disciplina.get_id_dis()] = Disciplina


    def sterge_dis(self, id_dis):
        if id_dis not in self.__lista_discipline:
            raise RepoError("Disciplina inexistenta!!!")
        del self.__lista_discipline[id_dis]

    def cauta_dis(self, id_dis):
        if id_dis not in self.__lista_discipline:
            raise RepoError("Disciplina inexistenta!!!")
        return self.__lista_discipline[id_dis]

    def modifica_dis(self, Disciplina):
        id_dis = Disciplina.get_id_dis()
        if id_dis not in self.__lista_discipline:
            raise RepoError("Disciplina existenta!!!")
        self.__lista_discipline[id_dis] = Disciplina


    def get_all(self):
        return [self.__lista_discipline[id_dis] for id_dis in self.__lista_discipline]







