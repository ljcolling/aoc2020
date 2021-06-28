
# parse a passport string
def parsePassport(passport):
    parsedPassport = dict()
    passport = passport.replace("\n"," ")
    for p in passport.split(" "):
        if p.find(":") != -1:
            parsedPassport[(p.split(":")[0]).strip("\n")] = p.split(":")[1].strip("\n")

    return parsedPassport


def checkInRange(value,min,max):
    value = int(value)
    validValues = range(min,max+1)
    return value in validValues



def test_checkInRange():
    assert checkInRange(1919,1920,2002) == False, "Should be False"
    assert checkInRange(2002,1920,2002) == True, "Should be True"
    assert checkInRange(2003,1920,2002) == False, "Should be False"
    assert checkInRange(1950,1920,2002) == True, "Should be True"
    assert checkInRange(2020,2020,2030) == True, "Should be True"

def parseHgt(hgtField):
    if (len(hgtField) == 5) & (hgtField.find("cm") != -1):
        value = hgtField[:3]
        units = "cm"
        return {"units": units, "value": int(value)}

    elif (len(hgtField) == 4) & (hgtField.find("in") != -1):

        value = hgtField[:2]
        units = "in"
        return {"units": units, "value": int(value)}
    else:
        return {"units": "xx", "value": 0}
    

def test_parseHgt():
    assert parseHgt('60in') == {'units':'in','value':60}
    assert parseHgt('190cm') == {'units':'cm','value':190}
    assert parseHgt('60cm') == {'units':'xx','value':0}
    assert parseHgt('600in') == {'units':'xx','value':0}



def validateHgt(hgtField):
    parsedHgt = parseHgt(hgtField)
    if parsedHgt["units"] == "in":
        return  checkInRange(parsedHgt["value"], 59, 76)
    elif parsedHgt["units"] == "cm":
        return  checkInRange(parsedHgt["value"], 150, 193)
    else:
        return False


def test_validateHgt():
    assert validateHgt('60in') == True, "Should be True"
    assert validateHgt('190cm') == True, "Should be True"
    assert validateHgt('190in') == False, "Should be False"
    assert validateHgt('190') == False, "Should be False"


def validateByr(byrField):
    return checkInRange(byrField,1920,2002)

def test_validateByr():
    assert validateByr(2002) == True, "Should be True"
    assert validateByr(2003) == False, "Should be False"


def validateIyr(iyrField):
    return checkInRange(iyrField,2010,2020)

def test_validateIyr():
    assert validateIyr(2010) == True, "Should be True"
    assert validateIyr(2012) == True, "Should be True"
    assert validateIyr(2020) == True, "Should be True"
    assert validateIyr(2015) == True, "Should be True"
    assert validateIyr(2002) == False, "Should be False"
    assert validateIyr(2021) == False, "Should be False"


def validateEyr(eyrField):
    return checkInRange(eyrField,2020,2030)


def test_validateEyr():
    assert validateEyr(2020) == True, "Should be True"
    assert validateEyr(2030) == True, "Should be True"
    assert validateEyr(2025) == True, "Should be True"
    assert validateEyr(2002) == False, "Should be False"
    assert validateEyr(2031) == False, "Should be False"


def validateHcl(hclField):
    if hclField[0] != "#":
        return False
    else:
        colour = hclField[1:]
        validChrs = ([str(x) for x in range(0,10)] + [chr(x) for x in range(ord('a'),ord('f')+1)])
        return all([c in validChrs for c in colour])

def test_validateHcl():
    assert validateHcl("#123abc") == True
    assert validateHcl("#123abz") == False
    assert validateHcl("123abc") == False

        
def validateEcl(eclField):
    return eclField in ['amb','blu','brn','gry','grn','hzl','oth']

def test_validateEcl():
    assert validateEcl("brn") == True
    assert validateEcl("wat") == False 


def validatePid(pidField):
    if len(pidField) != 9:
        return False
    else:
        validChrs = [str(x) for x in range(0,10)]
        return all([c in validChrs for c in pidField])

def test_validatePid():
    assert validatePid("000000001") == True
    assert validatePid("0123456789") == False 


def validateCid(cidField):
    return True



def checkFields(passport):
    parsedPassport = parsePassport(passport)
    hasFields = list(parsedPassport.keys())
    if 'cid' in hasFields:
        needsFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
        return (all([c in hasFields for c in needsFields]))
    else:
        needsFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
        return (all([c in hasFields for c in needsFields]))



def test_checkFields():
    x = """
    ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    byr:1937 iyr:2017 cid:147 hgt:183cm 
    """
    assert checkFields(x) == True
    
    x = """
    iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    hcl:#cfa07d byr:1929 
    """
    assert checkFields(x) == False

    x = """
    hcl:#ae17e1 iyr:2013
    eyr:2024
    ecl:brn pid:760753108 byr:1931
    hgt:179cm
    """
    assert checkFields(x) == True

    x = """
    hcl:#cfa07d eyr:2025 pid:166559648
    iyr:2011 ecl:brn hgt:59in
    """
    assert checkFields(x) == False


    x = """"
    pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f 
    """
    assert checkFields(x) == True


def checkPassport(passport):
    if checkFields(passport) == False:
        return False
    else:
        parsedPassport = parsePassport(passport)

        valids = []
        for f in list(parsedPassport.keys()):
            if eval("validate" + f.capitalize() + "('" + parsedPassport[f] + "')") == False:
                valids.append(False)
            else:
                valids.append(True)
        
        return all(valids) 



def test_checkPassport():

    x = """
    eyr:1972 cid:100
    hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
    """
    assert checkPassport(x) == False, "Should be false" 

    x = """
    iyr:2019
    hcl:#602927 eyr:1967 hgt:170cm
    ecl:grn pid:012533040 byr:1946
    """
    assert checkPassport(x) == False, "Should be false" 

    x = """
    hcl:dab227 iyr:2012
    ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
    """
    assert checkPassport(x) == False, "Should be false" 

    x = """
    hgt:59cm ecl:zzz
    eyr:2038 hcl:74454a iyr:2023
    pid:3556412378 byr:2007
    """
    assert checkPassport(x) == False, "Should be false" 


    x = """
    pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f
    """
    assert checkPassport(x) == True, "Should be true" 

    x = """
    eyr:2029 ecl:blu cid:129 byr:1989
    iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
    """
    assert checkPassport(x) == True, "Should be true" 

    x = """
    hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022
    """
    assert checkPassport(x) == True, "Should be true" 

    x = """
    iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

    """
    assert checkPassport(x) == True, "Should be true" 


if __name__ != "__main__":
    test_checkInRange()
    print("checkInRange() tests passed!")

    test_validateByr()
    print("validateByr() tests passed!")

    test_validateIyr()
    print("validateIyr() tests passed!")

    test_validateEyr()
    print("validateEyr() tests passed!")

    test_parseHgt()
    print("parseHgt() tests passed!")

    test_validateHgt()
    print("validateHgt() tests passed!")

    test_validateHcl()
    print("validateHcl() tests passed!")

    test_validateEcl()
    print("validateEcl() tests passed!")

    test_validatePid()
    print("validatePid() tests passed!")

    test_checkFields()
    print("checkFields() tests passed!")

    test_checkPassport()
    print("checkPasport() tests passed!")

    print("All tests passed!")


file = "puzzle_data.txt"
passports = []
count = 1


# First just count the number of passports
with open(file) as f:
    for line in f:
        if line == "\n":
            count = count + 1


passports = [''] * count
count = 0
with open(file) as f:
    for line in f:
        if line == "\n":
            count = count + 1

        passports[count] = passports[count] + " " + line.strip("\n")

ptI = 0
ptII = 0
for p in passports:
    ptI = ptI + int(checkFields(p))
    ptII = ptII + int(checkPassport(p))

print(ptI)
print(ptII)

