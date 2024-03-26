import sys, math
T = int(input()) 
nums = [int(sys.stdin.readline()) for i in range(T)]

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

for i in range(T):
    num1 = math.floor(nums[i]/2)
    num2 = math.ceil(nums[i]/2)
    res1,res2 = 0,0
    while num1 > 1:
        if (num1 == 2) and (num2 == 2):
            print(f'{num1} {num2}')
            break
        else:
            if prime(num1) and prime(num2):
                print(f'{num1} {num2}')
                break
            else:
                num1 -= 1
                num2 += 1
