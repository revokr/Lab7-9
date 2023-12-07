from Teste.Teste_student import teste_student
from Teste.Teste_discipline import teste_discipline
from Validator.Validator import validator_student,validator_dis
from UI.consola import Consola
from repo.repository import repo_student, repo_discipline
from business.service import ServiceStudent, ServiceDiscipline

if __name__ == "__main__":
    teste_std = teste_student()
    teste_std.ruleaza_toate_testele()
    teste_dis = teste_discipline()
    teste_dis.ruleaza_toate_testele()

    Repo_student = repo_student
    Validator_student = validator_student
    service_student = ServiceStudent(repo_student(), validator_student())
    service_dis = ServiceDiscipline(repo_discipline(), validator_dis())

    UI = Consola(service_student, service_dis)

    UI.run()