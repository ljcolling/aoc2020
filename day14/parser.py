line = 'mask = 100110X100000XX0X100X1100110X001X100'


line = 'mem[1005] = 121034'


if line[:3] == "mem":
    val = int(line.split("=")[0].split("[")[1].split("]")[0])
    loc = int(line.split("=")[1])
    return {location: loc, value: value}
else:
    return {mem: line.split("= ")[1]



