class Student:
    def __init__(self, student_id):
        self.__name = ''
        self.__age = 0
        self.__gender = None
        self.__student_id = student_id
        self.__courses = {}