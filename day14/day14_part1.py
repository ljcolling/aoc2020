# Day 14 Docking data

from numpy import binary_repr
def dec2bin(dec):
    return [x for x in binary_repr(dec,36)]

def applyMask(x):
    mask = x[0]
    value = x[1]
    if mask == 'X':
        return int(value)
    if mask == '0':
        return 0
    if mask == '1':
        return 1


def compute(mask, value, location):
    mask_bits = [x for x in mask]

    value = dec2bin(value)

    result = [applyMask(x) for x in zip(mask_bits,value) ]
    return {location: sum([x * (2 ** y) for x,y in zip(result, range(35,-1,-1))])}


def runcode(input, memory):
    memory[list(input.keys())[0]] = list(input.values())[0]
    return memory


def parse_line(line):
    if line[:3] == "mem":
        loc = int(line.split("=")[0].split("[")[1].split("]")[0])
        val = int(line.split("=")[1])
        return {"mem": {"location": loc, "value": val}}
    else:
        return {"mask": line.split("= ")[1]}

program = []

with open("puzzle_data.txt") as f:
    for line in f:
        program.append(parse_line(line))

memory = {}
mask = []
for p in program:
    if list(p.keys())[0] == "mask":
        mask = list(p.values())[0]
        print("updating mask")
    else:
        loc = p["mem"]["location"]
        val = p["mem"]["value"]
        print(f"running the code {val} at {loc}")
        memory = runcode(compute(mask,val,loc), memory)


print(sum(list(memory.values())))
