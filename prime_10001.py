# finding the 10,001st prime number
def is_prime(num):
    div_flag = 0
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            div_flag += 1
    if div_flag == 0:
        return True
    else:
        return False

ctr = 1
num_check = 3
while ctr < 10001:
    if is_prime(num_check):
        ctr += 1
    num_check += 2
    print num_check

print "10,001st prime is:" + str(num_check-2)
