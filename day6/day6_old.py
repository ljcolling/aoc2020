
# file = 'test_data.txt'
# file = "puzzle_data.txt"
file = "test2.txt"
declarations = []
count = 1


# First just count the number of declarations
with open(file) as f:
    for line in f:
        if line == "\n":
            count = count + 1




count

declarations = [''] * count
count = 0
with open(file) as f:
    for line in f:
        if line == "\n":
            count = count + 1

count = 0
with open(file) as f:
    for line in f:
        if line == "\n":
            count = count + 1

        this_dec = declarations[count] + "\n" + line.strip("\n")

        declarations[count] = this_dec



print(declarations[0])
print(declarations[1])
print(declarations[2])
print(declarations[3])
print(declarations[4])

yes = []
for dec in declarations:
    yes.append("".join(list(set(dec))))



for_sum =[]
for y in yes:
    for_sum.append(len(y))

print(sum(for_sum))
