
from itertools import compress
from functools import reduce
import copy

rules = {}
with open("rules.txt") as f:
    for line in f:
        rule = line.split(": ")[1].strip("\n")
        rule_name = line.split(": ")[0] 
        ranges = rule.split(" or ")
        range1 = range(int(ranges[0].split("-")[0]), int(ranges[0].split("-")[1]) + 1)
        range2 = range(int(ranges[1].split("-")[0]), int(ranges[1].split("-")[1]) + 1)
        rules[rule_name] = list(range1) + list(range2)

errors = []
tickets = []

with open("tickets.txt") as f:
  for line in f:
        ticket = [int(x) for x in line.split(",")]
        tickets.append(ticket)

def validateTicket(ticket, rules):
    valid_fields = []
    for field in ticket:
        valid_fields.append(any([field in rules[x] for x in list(rules.keys())]))        
    return all(valid_fields)


valid_tickets = []
for ticket in tickets:
    valid_tickets.append(validateTicket(ticket,rules))

tickets = list(compress(tickets, valid_tickets))
big_matches = []

for field in range(0,len(tickets[0])):
    matches = []
    for ticket in tickets:
        # print(f"field {field} of this ticket is {ticket[field]}")
        this_value = ticket[field]
        matched = list(compress(list(rules.keys()), \
        [this_value in x for x in [rules[x] for x in rules]]))
        # print(:matched)
        if matched != set():
            matches.append(matched)
    big_matches.append(matches)

field = []
for matches in big_matches:
     field.append(reduce(lambda x, y: x.intersection(y), [set(x) for x in matches]))

print(field)


n = [len(x) for x in field]
field = [list(f) for f in field]
fieldraw = copy.deepcopy(field)

def removeItem(input_list, item):
    # if len(input_list) == 1:
    #     return input_list
    # else:
    if item in input_list: 
        return input_list.remove(item)
    else: 
        return input_list


def findOne(input_list):
   return [f[0] for f in input_list if len(f) == 1][0]
 

removing = []
for i in range(0,19):
     r = findOne(field)
     removing.append(r)
     [removeItem(f,r) for f in field]
     field = [removeItem(f,r) for f in field]


def removeItem2(input_list, item):
    if len(input_list) == 1:
        return input_list
    else:
        if item in input_list: 
            return input_list.remove(item)
        else: 
            return input_list



for r in removing:
    [removeItem2(f, r) for f in fieldraw]
    fieldraw = [removeItem2(f, r) for f in fieldraw]


fields = [f[0] for f in fieldraw]

index1 = fields.index("departure track")
index2 = fields.index("departure date")
index3 = fields.index("departure location")
index4 = fields.index("departure platform")
index5 = fields.index("departure time")
index6 = fields.index("departure station")

my_ticket = [103,197,83,101,109,181,61,157,199,137,97,179,151,89,211,59,139,149,53,107]

ans = my_ticket[index1] * my_ticket[index2] * my_ticket[index3] * my_ticket[index4] * my_ticket[index5] * my_ticket[index6]
print(ans)
