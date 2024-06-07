n = int(input())
price = int(input())

for i in range(n-1):
    cal = input()
    if cal[0] == '-':
        cal = cal[1:]
        cal = int(cal)
        price -= cal
    else:
        price += int(cal)

print(price)