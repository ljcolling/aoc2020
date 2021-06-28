
# imports
import re
from itertools import chain

def parseBag(input):
    input = input.replace(",","").replace(".","")

    division = re.split(" contain", input)
    basebag = re.split(" bags?", division[0]).pop(0).strip()


    innerbags = re.split("bags?",division[1])

    innerbags = [bag.strip() for bag in innerbags if bag != ""]

    bag_array = []
    for bag in innerbags:
        if bag[1:].strip()=="o other":
            b = "other"
            n = 0
        else:
            b = bag[1:].strip()
            n = int(bag[0:1])
        
        bag_array.append({b: n})
        # bag_array.append({bag[1:].strip(): int(bag[0:1])})


    return {basebag: bag_array}


def test_parseBag():


    input = "light red bags contain 1 bright white bag, 2 muted yellow bags."
    output = {'light red': [{'bright white':1}, {'muted yellow':2}]}

    assert parseBag(input) == output
    print("parseBag() passed!")


filename = "input.txt"
# filename = "test_data.txt"
# filename = "test_data2.txt"
# Read in and parse the strings

def importRules(filename):
    # bags = dict()
    bags = []
    with open(filename) as f:
        for line in f:
            # bags.update(parseline(line))
            bags.append(line.strip())
    return bags


def parseline(line):
    # textstring = 'mirrored orange bags contain 2 dim green bags, 2 striped red bags, 4 drab plum bags, 1 pale teal bag.'
    textstring = line
    textstring = textstring.replace(",","")

    root = re.split(" contain", textstring)

    innerbags = re.split("bags?", root[1])
    # innerbags.remove(".")

    basebag = re.split(" bags?", root[0]).pop(0).strip()

    contains = []
    for bag in innerbags:
        bag = re.sub(r'\d+','',bag)
        contains.append(bag.strip())


    contains.pop()
    thisdict = {basebag: contains}
    return thisdict


bags = importRules(filename)

parsed_bags = dict()
for bag in bags:
    parsed_bags.update(parseBag(bag))


    

stack = []
all_bags  = []
this_bags = ["shiny gold"]
def getBags(this_bags):
    current_lot = []
    for this_bag in this_bags:
        for i in range(0,len(parsed_bags[this_bag])):
            current_lot.append(list(parsed_bags[this_bag][i].keys()) * list(parsed_bags[this_bag][i].values())[0])

    return list(chain.from_iterable(current_lot))



one_deep = getBags(["shiny gold"])
two_deep = getBags(one_deep)

all_bags = [] 
current_bags = ["shiny gold"]

while current_bags != []:

    current_bags = getBags(current_bags)
    all_bags.append(current_bags)



print(len(list(chain.from_iterable(all_bags))))

