from domain.disciplina import disciplina
from Exceptii.ValidError import ValidError
from Exceptii.RepoError import RepoError
from Exceptii.UIError import UIError

class Consola:
    def __UI_sterge_student(self, params):
        if len(params) != 1:
            raise UIError("numar de parametrii gresit")
        id_std = int(params[0])
        self.__service_students.sterge_student(id_std)
    def __UI_adauga_student(self,params):
        if len(params) != 2:
            raise UIError("numar de parametrii gresit!")
            return
        try:
            id_student = int(params[0])
            nume_student = params[1]
            self.__service_students.adauga_student(id_student, nume_student)
        except ValueError:
            raise UIError("valori incorecte")
            return

    def __UI_modifica_student(self, params):
        if len(params) != 2:
            raise UIError("numar de parametrii gresit!")
        id = int(params[0])
        nume = params[1]
        self.__service_students.modifica_std(id, nume)

    def __UI_cauta_student(self, params):
        if len(params) != 1:
            raise UIError("numar de parametrii gresit!")
        id = int(params[0])
        self.__service_students.cauta_std(id)

    def __UI_print_studenti(self,params):
        studenti = self.__service_students.get_all_studenti()
        if len(studenti) == 0:
            raise UIError("nu exista studenti")
        for Student in studenti:
            print(Student.get_id_student(), ",", Student.get_nume_student())

    def __UI_adauga_disciplina(self, params):
        if len(params) != 4:
            raise UIError("numar de parametrii gresit!")
        try:
            id_dis = int(params[0])
            nume_dis = params[1]
            nume_prof = params[2] + " " + params[3]
            self.__service_discipline.adauga_disciplina(id_dis, nume_dis, nume_prof)
        except ValueError:
            raise UIError("valori incorecte")

    def __UI_sterge_disciplina(self, params):
        if len(params) != 1:
            raise UIError("numar de parametrii gresit")
        id_dis = int(params[0])
        self.__service_discipline.sterge_disciplina(id_dis)

    def __UI_modifica_dis(self, params):
        if len(params) != 4:
            raise UIError("numar de parametrii gresit")
        id = int(params[0])
        nume = params[1]
        nume_prof = params[2] + " " + params[3]
        self.__service_discipline.modifica_disciplina(id, nume, nume_prof)

    def __UI_cauta_dis(self, params):
        if len(params) != 1:
            raise UIError("numar de parametrii gresit!")
        id = int(params[0])
        dis = self.__service_discipline.cauta_disciplina_id(id)
        print(dis.get_id_dis(),",", dis.get_nume_dis(),",", dis.get_profesor())

    def __UI_print_discipline(self, params):
        Discipline = self.__service_discipline.get_all_discipline()
        if len(Discipline) == 0:
            raise UIError("nu exista discipline!")
        for disciplinna in Discipline:
            print(disciplinna.get_id_dis(),",", disciplinna.get_nume_dis(),",", disciplinna.get_profesor())

    def __init__(self, service1, service2):
        self.__service_discipline = service2
        self.__service_students = service1
        self.__commands = {
            "adauga_student":self.__UI_adauga_student,
            "print_studenti":self.__UI_print_studenti,
            "sterge_student":self.__UI_sterge_student,
            "modifica_student":self.__UI_modifica_student,
            "cauta_student":self.__UI_cauta_student,
            "adauga_dis":self.__UI_adauga_disciplina,
            "sterge_dis":self.__UI_sterge_disciplina,
            "modifica_dis":self.__UI_modifica_dis,
            "cauta_dis":self.__UI_cauta_dis,
            "print_dis":self.__UI_print_discipline
        }


    def run(self):
        while True:
            command = input("cmd>>>")
            command = command.strip()
            if command == "":
                continue
            if command == "exit":
                return
            parts = command.split()
            command_name = parts[0]
            params = parts[1:]
            if command_name in self.__commands:
                try:
                    self.__commands[command_name](params)
                except ValidError:
                    raise ValidError("valori necurate")
                except RepoError as re:
                    raise RepoError("repo error")
            else:
                print("comanda invalida!")