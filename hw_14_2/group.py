class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        return self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        group_list = []

        for student_ in self.group:
            group_list.append(student_.last_name)

            if last_name in group_list:
                return student_

    def __str__(self):
        all_students = ''
        self.number = 0

        for everyone_ in self.group:
            self.number += 1
            all_students += everyone_.last_name + ' '

        return f'Number:{self.number}\n{all_students}\n'