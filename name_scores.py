# name scores problem

with open('name_score.txt', 'r') as myfile:
    data = myfile.read()

names_array = data.split(',')
names_array.sort()
full_final = 0
names_array = [name.upper().strip('\"') for name in names_array]


def calculate_score(name_1):
    add = 0
    for character in name_1:
        add += (ord(character) - 64)
    return add

full_final = 0

for name_1 in names_array:
    calc = calculate_score(name_1)
    final_name = calc * (names_array.index(name_1)+1)
    full_final += final_name
print full_final
