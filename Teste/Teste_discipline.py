from repo.repository import repo_discipline
from domain.disciplina import disciplina
from Validator.Validator import validator_dis
from Exceptii.ValidError import ValidError


class teste_discipline:

    def ruleaza_toate_testele(self):
        self.__teste_domain()
        self.__test_validare()
        self.__teste_repo_disciplina()


    def __teste_domain(self):
        print("Start teste domain Disciplina...")
        id_disc = 321
        nume_disc = "Chimie"
        nume_prof = "Busteaga"

        Disciplina = disciplina(id_disc, nume_disc,nume_prof)

        assert Disciplina.get_id_dis() == id_disc
        assert Disciplina.get_profesor() == nume_prof
        assert Disciplina.get_nume_dis() == nume_disc
        print("    _Sfarsit teste domain Disciplina.\n")

    def __test_validare(self):
        print("Start teste validare Disciplina...")
        validator = validator_dis()
        id_disc = 312
        nume_disc = "Mate"
        nume_prof = "Andrei"
        Disciplina = disciplina(id_disc, nume_disc, nume_prof)

        validator.valideaza_dis(Disciplina)

        id_disc_X = -4
        nume_disc_X = ""
        nume_prof_X = ""

        Disciplina_X = disciplina(id_disc_X, nume_disc_X, nume_prof_X)

        try:
            validator.valideaza_dis(Disciplina_X)
            assert False
        except ValidError as ve:
            assert str(ve) == "ID disciplina invalid\nNume disiplina invalid\nNume profesor invalid"
        print("    _Sfarsit teste validare Disciplina\n")

    def __teste_repo_disciplina(self):
        print("Start teste repo Disciplina...")
        repo_disc = repo_discipline()
        id_disc = 312
        nume_disc = "Mate"
        nume_prof = "Andrei"
        Disciplina = disciplina(id_disc, nume_disc, nume_prof)

        repo_disc.adauga_dis(Disciplina)
        assert len(repo_disc) == 1

        id_disc_1 = 31
        nume_disc_1 = "Chimie"
        nume_prof_1 = "Busteaga"
        Disciplina1 = disciplina(id_disc_1, nume_disc_1, nume_prof_1)
        repo_disc.adauga_dis(Disciplina1)
        assert len(repo_disc) == 2

        repo_disc.sterge_dis(id_disc)
        assert len(repo_disc) == 1


        assert repo_disc.cauta_dis(id_disc_1) == Disciplina1

        id_disc_nou = 31
        nume_disc_nou = "Biologie"
        nume_prof_nou = "Husca"
        Disciplina_nou = disciplina(id_disc_nou, nume_disc_nou, nume_prof_nou)
        repo_disc.modifica_dis(Disciplina_nou)

        assert repo_disc.cauta_dis(id_disc_1) == Disciplina_nou

        print("    _Sfarsit teste repo Disciplina.\n")