# known_people = ["Harry", "Larry", "Role"]
# person = raw_input("Enter the person you known: ")
#
# if person in known_people:
#     print("you know {}!".format(person))
# else:
#     print("don't known {}!".format(person))

def who_do_you_know():
    persons_you_know = raw_input("Enter all the person you know split by comma: ")
    persons_list = persons_you_know.split(",")

    persons_without_spaces = []
    for person in persons_list:
        persons_without_spaces.append(person.strip())
    return persons_without_spaces

def ask_user():
    user_input_name = raw_input("enter a name you want to check: ")
    if user_input_name in who_do_you_know():
        print "you know {}!".format(user_input_name)
    else:
        print "you don't know {}!".format(user_input_name)

ask_user()
