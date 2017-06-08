lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 2)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name,
        self.numbers = (5, 9, 12, 3, 1, 2)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Rolf")
player_two = LotteryPlayer("John")
# print (player_two)

##


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def avg(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print ("I am going to school!")


anna = Student("Anna", "MIT")
anna.marks.append(90)
anna.marks.append(77)

print (Student.go_to_school())
