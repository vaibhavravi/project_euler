# find path through pyramid problem 67 and 18

import time

start_time = time.time()

with open('pyr_100.txt', 'r') as myfile:
    data = myfile.read()

numbers = data.split('\n')

array2 = []
final_array = []

for i in numbers:
    array1 = numbers[numbers.index(i)].split(' ')
    array2 = []
    for j in array1:
        array2.append(float(j))
    final_array.append(array2)

nRows = len(final_array)
cRow = nRows - 1
pRow = cRow - 1

for ctr in reversed(xrange(nRows)):
    pos = 0
    cRow = ctr
    pRow = cRow - 1
    for iC in final_array[cRow]:
        if pos < len(final_array[cRow])-1:
            iN = final_array[cRow][pos+1]
            iP = final_array[pRow][pos]
            iPNew = max(iC+iP, iN+iP)
            final_array[pRow][pos] = iPNew
        pos += 1
    if ctr == 1:
        break

stop_time = time.time()

print stop_time-start_time
print final_array[0]
