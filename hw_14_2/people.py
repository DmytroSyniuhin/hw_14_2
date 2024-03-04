class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'I am {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return self.last_name

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.__str__() == other.__str__()
        return NotImplemented

    def __hash__(self):
        return hash(str(self))

