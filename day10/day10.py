

x = []
x.append(0)
with open("puzzle_data.txt") as f:
    for line in f:
        x.append(int(line))

x.append(max(x) + 3)

checked = {}

def find_route(i):

    if (i in x) == False:
        return 0
   
    if i in checked:
        return checked[i]

    if i == max(x):
        return 1

    routes = 0

    checked[i + 1]  = find_route(i + 1)
    checked[i + 2]  = find_route(i + 2)
    checked[i + 3]  = find_route(i + 3)
    routes = routes + checked[i + 1] + checked[i + 2] + checked[i + 3]
    
    return routes




print(find_route(0))
