# imports

import re


# Steps 
# Read in and parse the strings

def readtext():
    
    bags = dict()

    filename = "input.txt"
    with open(filename) as f:
        for line in f:
            bags.update(parseline(line))
   
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


bags = readtext()


BAGS = ['shiny gold']

new = 0
end_this = False
while end_this == False:
    current = new
    for bag in bags.keys():
        if [value for value in BAGS if value in bags[bag]]:
            BAGS.append(bag)

    new = len(list(set(BAGS)))-1
    if new == current:
        end_this = True


print(len(list(set(BAGS)))-1)
