num = 11

def prime(num):
    ii = 2
    while ii < num:
        remainder = num % ii
        if remainder == 0:
            ii += 1
            break
        ii += 1
    if ii == num:
        return True
    else:
        return False

print(prime(num))