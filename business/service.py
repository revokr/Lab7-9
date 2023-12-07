from domain.student import student
from domain.disciplina import disciplina
from repo.repository import repo_student,repo_discipline
from Validator.Validator import validator_student, validator_dis

class ServiceStudent:
    def __init__(self, repo, valid):
        self.__Repo_student = repo
        self.__Validator_student = valid

    def adauga_student(self, id_student, nume_student):
        Student = student(id_student, nume_student)
        self.__Validator_student.valideaza_std(Student)
        self.__Repo_student.adauga_std(Student)
        return Student

    def sterge_student(self, id_student):
        self.__Repo_student.sterge_std(id_student)

    def cauta_std(self, id_student):
        return self.__Repo_student.cauta_student(id_student)

    def modifica_std(self, id_student, nume_student):
        std = student(id_student, nume_student)
        self.__Repo_student.modifica_student(std)
        return std

    def get_all_studenti(self):
        return self.__Repo_student.get_all()

    def get_len(self):
        return len(self.__Repo_student)

class ServiceDiscipline:
    def __init__(self, repo, valid):
        self.__Repo_discipline  = repo
        self.__Validator_discipline = valid

    def adauga_disciplina(self, id_dis, nume_dis, nume_prof):
        Disciplina = disciplina(id_dis, nume_dis, nume_prof)
        self.__Validator_discipline.valideaza_dis(Disciplina)
        self.__Repo_discipline.adauga_dis(Disciplina)


    def sterge_disciplina(self, id_dis):
        return self.__Repo_discipline.sterge_dis(id_dis)

    def cauta_disciplina_id(self, id_dis):
        self.__Repo_discipline.cauta_dis(id_dis)

    def modifica_disciplina(self, id, nume, nume_prof):
        dis = disciplina(id, nume, nume_prof)
        self.__Repo_discipline.modifica_dis(dis)
        return dis

    def get_len(self):
        return len(self.__Repo_discipline)
    def get_all_discipline(self):
        return self.__Repo_discipline.get_all()


