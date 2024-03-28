import sys

N = int(sys.stdin.readline().strip())
li_N = sys.stdin.readline().split()
set_N = set(li_N)
M = int(sys.stdin.readline().strip())
li_M = sys.stdin.readline().split()

def search_item(item, item_list):
    return 1 if item in item_list else 0
    

for i in li_M:
    print(search_item(i,set_N))


