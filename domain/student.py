class student:
    def __init__(self, id_student, nume_student):
        self.__id_student = id_student
        self.__nume_student = nume_student

    def get_id_student(self):
        return self.__id_student

    def get_nume_student(self):
        return self.__nume_student