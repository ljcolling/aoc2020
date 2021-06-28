rules = []
with open("rules.txt") as f:
    for line in f:
        rule = line.split(": ")[1].strip("\n")
        ranges = rule.split(" or ")
        range1 = range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]) + 1)
        range2 = range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]) + 1)
        rules.append(list(range1) + list(range2))

print(rules)

