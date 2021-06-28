#!/Users/lc663/.pyenv/shims/python

from numpy import binary_repr
from functools import reduce


def process(mask,i):
    if i == "X":
        mask0 = []
        for m in mask:
            mask0.append(m + "0")
            mask0.append(m + "1")
    else:
        mask0 = []
        for m in mask:
            mask0.append(m + i)

    return mask0

def mask2dec(mask):
    masklist = [int(x) for x in mask]
    return sum([x * (2 ** y) for x, y in zip(masklist, range(35,-1,-1))])


def applyMask(x):
    mask = x[0]
    value = x[1]
    if mask == 'X':
        return 'X'
    if mask == '0':
        return value
    if mask == '1':
        return '1'



def compute(mask, address, value, memory):

    address = binary_repr(address, 36)
    result = [applyMask(x) for x in zip(mask,address)]

    result = str(reduce(lambda x,y: str(x) + str(y), result))

    address = [""]
    for i in result:
        address = process(address, i)

    new_address = [mask2dec(x) for x in address]
    for a in new_address:
        memory[a] = value

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
    else:
        loc = p["mem"]["location"]
        val = p["mem"]["value"]
        memory = compute(mask, loc, val, memory)


print(sum(list(memory.values())))

