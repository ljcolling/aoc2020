import copy
# file = 'test_data.txt'
file = 'puzzle_data.txt'

programRaw = []
with open(file) as f:
    for line in f:
        op, arg = line.strip("\n").split(" ")
        instruction = [op, int(arg)]
        programRaw.append(instruction)




pointer = 0
op = ""
acc = 0
i = 0
# print("Program length: ", len(program))

# for c in range(0,100):
# for c in [1]:
def runTest(c, program):
    # print("c :" + str(c))
    # print("program: ")
    # print(program)
    count = 0
    i = 0
    acc = 0
    op = ""
    acc = 0
    pointer = 0
    while op != None:
        i = i + 1
        
        if pointer == len(program) :
            print("ACC : " + str(acc))
            return acc
        op = program[pointer][0]
        arg = program[pointer][1]
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
       
        
        if op == "jmp":
            count = count + 1
            if (count == c):
                    op = "nop"
                    program[pointer][0] = op

            
        acc, pointer = processIntruction(op, arg, acc, pointer)

    return None

i = 0
acc = None
while i < 10: # just limit it so it doesn't run too long
    acc = runTest(i, copy.deepcopy(programRaw.copy()))
    i = i + 1
    if acc != None:
        break

