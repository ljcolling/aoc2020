
file = 'test_data.txt'
file = 'puzzle_data.txt'

program = []
with open(file) as f:
    for line in f:
        op, arg = line.strip("\n").split(" ")
        instruction = [op, int(arg)]
        program.append(instruction)



def processIntruction(op, arg, acc, pointer):
    if op == "acc":
        acc = acc + arg
        program[pointer][0] = None
        pointer = pointer + 1
        return acc, pointer
    if op == "jmp":
        program[pointer][0] = None
        pointer = pointer + arg
        return acc, pointer
    if op == "nop":
        program[pointer][0] = None
        pointer = pointer + 1
        return acc, pointer 
    else:
        return acc, pointer

pointer = 0
op = ""
acc = 0
i = 0
while op != None:
    i = i + 1
    op = program[pointer][0]
    arg = program[pointer][1]
   
    acc, pointer = processIntruction(op, arg, acc, pointer)

print(acc)



