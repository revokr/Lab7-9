from domain.student import student
from repo.repository import repo_student
from Validator.Validator import validator_student
from Exceptii.ValidError import ValidError


class teste_student:
    def ruleaza_toate_testele(self):
        self.__test_domain()
        self.__teste_validare()
        self.__test_repo_studenti()



    def __test_domain(self):
        print("Start teste domain Student...")
        id_std = 41
        nume_std = "paul"
        std = student(id_std, nume_std)
        assert (std.get_id_student() == id_std)
        assert (std.get_nume_student() == nume_std)
        print("    _Sfarsit teste domain Student.\n")


    def __test_repo_studenti(self):
        print("Start teste repo Student...")
        id_std = 21
        nume_std = "hopa mitica"
        std = student(id_std, nume_std)
        repo_std = repo_student()
        assert repo_std.is_empty()
        repo_std.adauga_std(std)
        assert len(repo_std) == 1
        id_std1 = 43
        nume_std1 = "gigel"
        std1 = student(id_std1, nume_std1)
        repo_std.adauga_std(std1)
        assert len(repo_std) == 2
        repo_std.sterge_std(id_std)
        assert len(repo_std) == 1
        assert repo_std.cauta_student(id_std1) == std1

        id_std_nou = 43
        nume_std_nou = "mircea"
        std_nou = student(id_std_nou, nume_std_nou)
        repo_std.modifica_student(std_nou)
        assert repo_std.cauta_student(id_std_nou) == std_nou

        studentz = repo_std.get_all()
        assert len(studentz) == 1
        assert studentz[0].get_id_student() == 43
        print("    _Sfarsit teste repo Student.\n")

    def __teste_validare(self):
        print("Start teste validare Student...")
        validator = validator_student()
        id_std = 34
        nume_std = "gigel"
        std = student(id_std, nume_std)

        validator.valideaza_std(std)

        id_std_X = -54
        nume_std_X = ""

        std_X = student(id_std_X, nume_std_X)
        try:
            validator.valideaza_std(std_X)
            assert False
        except ValidError as ex:
            assert str(ex)  == "ID student invalid\nnume invalid"
        print("    _Sfarsit teste validare Student.\n")


