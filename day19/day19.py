
rules = {}
rules[0] = [1, 2]
rules[1] = "a"
rules[2] = [[1, 3], [3, 1]]
rules[3] = "b"


rules = {}
rules[0] = [4, 1, 5]
rules[1] = [2, 3]
rules[2] = [4, 4]
rules[3] = [4, 5]
rules[4] = "a"
rules[5] = "b"
print(len(rules[0]))

messages = [] 
def do(x,message):
    if x == 4:
        return "a"
    if x == 5:
        return "b"
    if isinstance(rules[x][0], int) == False:
        messages.append(message + str(do(rules[x][0][0], message)) + str(do(rules[x][1][0], message)))
        messages.append(message + str(do(rules[x][0][1], message)) + str(do(rules[x][1][1], message)))
    else:
        if len(rules[x]) == 2:
            message = message + str(do(rules[x][0], message)) + str(do(rules[x][1], message))
        elif len(rules[x]) == 3:
            message = message + str(do(rules[x][0], message)) + str(do(rules[x][1], message) + str(do(rules[x][2], message)))
    return message

message = do(0,"")
print(message)
print(messages)
