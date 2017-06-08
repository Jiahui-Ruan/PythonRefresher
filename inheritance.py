class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args, **kwargs):
        #return a new Student
        return cls(friend_name, origin.school, *args, **kwargs)

##

class WorkingStudent(Student, object):
    def __init__(self, name, school, salary):
        super(WorkingStudent, self).__init__(name, school)
        self.salary = salary

anna = WorkingStudent("Anna", "MIT", 3000)

friend = WorkingStudent.friend(anna, "Greg", 17.50)
print(friend.name)
print(friend.school)
print(friend.salary)
