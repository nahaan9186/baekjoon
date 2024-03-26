N = int(input())
nums = input().split()
cnt = N

for i in range(len(nums)):
    num = int(nums[i])
    if num == 1:
        cnt -= 1
        continue
    if num == 2:
        continue
    ii = 2
    while ii < num:
        remainder = num % ii
        if remainder == 0:
            cnt -= 1
            ii += 1
            break
        ii += 1

print(cnt)