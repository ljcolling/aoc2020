
# file = 'test_data.txt'
# file = "puzzle_data.txt"


file = "test2.txt"
def loadData(file):
    declarations = []
    count = 1


    with open(file) as f:
        for line in f:
            if line == "\n":
                count = count + 1




    count

    declarations = [''] * count
    count = 0
    with open(file) as f:
        for line in f:
            if line == "\n":
                count = count + 1

    count = 0
    with open(file) as f:
        for line in f:
            if line == "\n":
                count = count + 1

            this_dec = declarations[count] +  line

            declarations[count] = this_dec
    
    return declarations



# yes = []
# for dec in declarations:
#     yes.append("".join(list(set(dec))))



# for_sum =[]
# for y in yes:
#     for_sum.append(len(y))

    
def countGroup(x):
    x = x.split("\n")
    i = 0
    for l in x:
        if l != "":
            i = i + 1 
    
    return i

def test_countGroup():
    declarations = loadData(file)
    x = declarations[0]
    assert countGroup(x) == 1


    x = declarations[1]
    assert countGroup(x) == 3


    x = declarations[2]
    assert countGroup(x) == 2

    x = declarations[3]
    assert countGroup(x) == 4



    x = declarations[4]
    assert countGroup(x) == 1

    print("countGroup() passed!")



def uniqueResponses(x):
    
    x = list(set(x))
    x.remove("\n")
    x.sort()
    return x

def test_uniqueResponses():
    
    declarations = loadData(file)
    x = declarations[0]
    assert uniqueResponses(x) == ['a','b','c']

    x = declarations[2]
    assert uniqueResponses(x) == ['a','b','c']
    print("uniqueResponses() passed!")





def countInstances(x):
    n = countGroup(x)
    answered = uniqueResponses(x)
    responses = ""
    for l in x:
        responses = responses + l.strip("\n")

    output = dict() 
    for a in answered:
        output.update({a: responses.count(a)})

    return output

def test_countInstances():
    
    declarations = loadData(file)
    x = declarations[0]
    
   
    assert countInstances(x) == {'a': 1, 'b': 1, 'c': 1}

    x = declarations[2]
    assert countInstances(x) == {'a': 2, 'b': 1, 'c': 1}
    print("countInstances() passed!")




def countAllAnswered(counts, groupSize):
    i = 0
    for c in counts:
        if counts[c] == groupSize:
            i = i + 1
    return(i)



def test_countAllAnswered():
    counts = {'a': 2, 'b': 1, 'c': 1}
    groupSize = 2
    assert countAllAnswered(counts,groupSize) == 1
    print("countAllAnswered() passed!")


def count(x):
    
    return countAllAnswered(countInstances(x), countGroup(x)) 

def test_count():
    declarations = loadData(file)

    x = declarations[0]
    assert count(x) == 3

    x = declarations[1]
    assert count(x) == 0

    x = declarations[2]
    assert count(x) == 1

    x = declarations[3]
    assert count(x) == 1

    x = declarations[4]
    assert count(x) == 1
    print("count() passed!")



# test_countGroup()
# test_uniqueResponses()
# test_countInstances()
# test_countAllAnswered()
# test_count()


sum = 0

declarations = loadData("puzzle_data.txt")
for x in declarations:
    sum = sum + count(x)

print(sum)

