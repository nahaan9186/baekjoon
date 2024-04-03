import sys

inputs = []
while True:
    item = sys.stdin.readline().rstrip()
    if item == '':
        break
    else:
        inputs.append(item)

count_nodes = inputs[0].split()[0]        
count_edges = inputs[0].split()[1]   
map = []     
for item in inputs[1:]:
    map.append(item.split())

print(map)


