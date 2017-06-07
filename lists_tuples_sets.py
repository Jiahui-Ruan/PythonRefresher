# lists are allowed to change while tuples are not allowed

grades = [99, 88, 100, 77] #list append and set add api diff
tuple_grades = (77, 90, 100, 80) #immutable
set_grades = {77, 80, 90} # set are unordered and unique

tuple_grades = tuple_grades + (100,) #must have comma at the end
# print(tuple_grades)

your_numbers = {1, 3, 5, 6, 8}
winning_numbers = {1, 3, 5, 7, 9}

print(your_numbers.intersection(winning_numbers))
