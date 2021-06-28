
from itertools import compress
from functools import reduce
# rules = {}
rules = []
with open("rules.txt") as f:
    for line in f:
        rule = line.split(": ")[1].strip("\n")
        ranges = rule.split(" or ")
        range1 = range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]) + 1)
        range2 = range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]) + 1)
        rules.append(list(range1) + list(range2))

errors = []
tickets = []
with open("tickets.txt") as f:
  for line in f:
        ticket = [int(x) for x in line.split(",")]
        tickets.append(ticket)

for ticket in tickets:
    for field in ticket:
        checks_passed = 0
        for rule in rules:
            if field in rule:
                checks_passed =+ 1
        if checks_passed == 0:
            errors.append(field)

rules = {}
rules["class"] = list(range(0,1+1)) + list(range(4,19+1))
rules["row"] = list(range(0,5+1)) + list(range(8,19+1))
rules["seat"] = list(range(0,13+1)) + list(range(16,19+1))

tickets = [[3, 9, 18], [15, 1, 5], [5, 14, 19]]
# # matches = [[[],[],[]],[[],[],[]],[[],[],[]]]
# matches = [[]] * 3
# t = 0
# for ticket in tickets:
#     t = t + 1 
#     n = 0
#     for field in ticket:
#         n = n + 1
#         for rule in rules:
#             rulename = rule
#             rulevalue = rules[rule]
#             if field in rulevalue:
#                 # print(f"field {n} on ticket {t} matches rule {rulename}")
#                 matches[t-1].append({n: rulename})
#                 # matches[t-1].append({rulename: n})


# def has_key(x,key):
#     if key in x.keys():
#         return x[key]
#     else:
#         return None

# matches = [[]] * 3
# t = 0
# for ticket in tickets:
#     t = t + 1 
#     n = 0
#     for field in ticket:
#         n = n + 1
#         if field in rules["seat"]:
#             # print(f"field {n} on ticket {t} matches rule for row")
#             matches[t-1].append({n: "seat"})
#             # matches[t-1].append({rulename: n})

# print(matches)
big_matches = []
for field in range(0,3):
    matches = []
    for ticket in tickets:
        print(f"field {field} of this ticket is {ticket[field]}")
        this_value = ticket[field]
        matched = list(compress(list(rules.keys()), [this_value in x for x in [rules[x] for x in rules]]))
        matches.append(matched)
    big_matches.append(matches)

field = [] 
for matches in big_matches:
    field.append(reduce(lambda x, y: x.intersection(y), [set(x) for x in matches]))

print(field)


