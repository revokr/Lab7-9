from Exceptii.ValidError import ValidError
class validator_student:
    def valideaza_std(self, Student):
        erori = ""
        if Student.get_id_student() < 0:
            erori += "ID student invalid\n"
        if Student.get_nume_student() == "":
            erori += "nume invalid"
        if len(erori) > 0:
            raise ValidError(erori)



class validator_dis:
    def valideaza_dis(self, Disciplina):
        erori = ""
        if Disciplina.get_id_dis() < 0:
            erori += "ID disciplina invalid\n"
        if Disciplina.get_nume_dis() == "":
            erori += "Nume disiplina invalid\n"
        if Disciplina.get_profesor() == "":
            erori += "Nume profesor invalid"
        if len(erori) > 0:
            raise ValidError(erori)