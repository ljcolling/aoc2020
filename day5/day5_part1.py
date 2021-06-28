
# file = 'test_data.txt'
file = "puzzle_data.txt"
passes = []

with open(file) as f:
    for line in f:
       passes.append(line.strip("\n")) 






IDs = []

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half+1:]

for thispass in passes:
    C = range(0,127)
    part1 = thispass[:7]
    for p in part1:
       F, B = split_list(C) 
       if p == "F":
           C = F
       elif p == "B": 
           C = B


    Z = range(0,7)
    part2 = thispass[7:]
    for p in part2:
       L, R = split_list(Z)
       if p == "L":
           Z = L
       elif p == "R":
           Z = R

    IDs.append(C.stop * 8 + Z.stop)



print(max(IDs))

IDs.sort()
print(IDs)

IDs_plus1 = [i + 1 for i in IDs]
IDs_minus1 = [i - 1 for i in IDs]

list1 = list(set(IDs_minus1) - set(IDs))
list2 = list(set(IDs_plus1) - set(IDs))

print(list1)
print(list2)
