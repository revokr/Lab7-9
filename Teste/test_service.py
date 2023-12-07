from domain.student import student
from business.service import ServiceStudent, ServiceDiscipline
class test_service_std:
    def __init__(self, repo, valid):
        self.__service = ServiceStudent(repo, valid)

    def reuleaza_teste_srv_std(self):
        self.__teste()

    def __teste(self):
        print("Start teste service studenti...")
        id = 32
        nume = "fafa"
        std = self.__service.adauga_student(id, nume)
        assert (self.__service.get_len() == 1)
        assert self.__service.cauta_std(id) == std
        self.__service.sterge_student(id)
        assert self.__service.get_len() == 0
        id1 = 4
        nume1 = "dasd"
        std1 = self.__service.adauga_student(id1, nume1)
        id2 = 5
        nume2 = "asdasda"
        std2 = self.__service.adauga_student(id2, nume2)
        students = self.__service.get_all_studenti()
        assert len(students) == 2
        id3 = 4
        nume3 = "gggggg"
        std3 = self.__service.modifica_std(id3, nume3)
        assert self.__service.cauta_std(id1) == std3


        print("    Sfarsit teste service studenti.\n")



class teste_service_dis:
    def __init__(self, repo, valid):
        self.__service_dis = ServiceDiscipline(repo, valid)


    def ruleaza_teste_srv_dis(self):
        print("Start teste service discipline...")
        self.__teste_srv_dis_adauga()
        self.__teste_srv_dis_sterge()
        self.__teste_srv_dis_modifica()
        print("    Sfarsit teste service discipline.")


    def __teste_srv_dis_adauga(self):
        id = 1
        nume = "mate"
        nume_prof = "adadn dasda"
        dis = self.__service_dis.adauga_disciplina(id, nume, nume_prof)
        assert self.__service_dis.get_len() == 1

    def __teste_srv_dis_sterge(self):
        id1 = 7
        nume1 = "jghiolban"
        nume_prof1 = "dasd gicu"
        dis1 = self.__service_dis.adauga_disciplina(id1, nume1, nume_prof1)
        self.__service_dis.sterge_disciplina(id1)
        assert self.__service_dis.get_len() == 1

    def __teste_srv_dis_modifica(self):
        id = 4
        nume = "mate"
        nume_prof = "adadn dasda"
        dis = self.__service_dis.adauga_disciplina(id, nume, nume_prof)
        assert self.__service_dis.cauta_disciplina_id(id) == dis
        id1 = 4
        nume1 = "romana"
        nume_prof1 = "marinov"
        self.__service_dis.modifica_disciplina(id1, nume1, nume_prof1)
        assert self.__service_dis.cauta_disciplina_id(id1) == dis
