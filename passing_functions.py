def methodception(another):
    return another()

def add_two_num():
    return 35 + 77

#print(methodception(add_two_num))

#print(methodception(lambda: 35 + 77)) #lambda function always has to be 1 line
my_list = [13, 22, 44, 89]
print(list(filter(lambda x: x != 13, my_list)))

print((lambda x: x * 5)(3))
