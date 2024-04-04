# N = input()

def recursion(n, i = 0):
    
    a = '____'*(i)  
    if i == 0:
        print(f'{a}A')  
    
    print(f'{a}B')
    if i == n:
        return print(f'{a}D\n{a}E')
    print(f'{a}C')
    recursion(n, i+1)
    print(f'{a}E')

    

recursion(2)