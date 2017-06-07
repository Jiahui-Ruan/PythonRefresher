my_string = "hello, world!"

# for character in my_string: #iterables are strings, lists, tuples, and sets
#     print character

my_list = [1, 3, 5, 6, 7]

for number in my_list:
    print(number ** 2)

user_wants_number = True
while user_wants_number == True:
    print 10

    user_input = raw_input("Should we print again? (Y/N)")
    if user_input == 'N':
        user_wants_number = False
