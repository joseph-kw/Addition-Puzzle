# Get the number
def get_num(string,mapping):
    output = 0
    for i in string:
        output *= 10
        output += mapping[i]
    return output

# Checking a Solution
def check_puzzle(*args):
    strT = ''
    words = []
    for char in args[:-1]:
        strT += str(char)
        words.append(char)
    mapping = args[-1]
    for i in strT:
        if i not in mapping.keys():
            return False 
    for k in words:
        if mapping[k[0]] == 0:
            return False
    for j in mapping.keys():
        if list(mapping.values()).count(mapping[i]) > 1:
            return False
    total = args[-2]
    add = args[:-2]
    add2 = 0
    for word in add:
        add2 += get_num(word,mapping)
    if add2 == get_num(total,mapping):
        return True
    return False

# Solving the puzzle
def addition_puzzle(*args):
    lst = []
    for i in args:
        lst += str(i)
    lst2 = list(set(lst))
    combi = 10**len(lst2)
    for j in range(combi):
        d1 = {}
        for k in lst2:
            d1[k] = j % 10
            j=j//10
            if check_puzzle(args,d1) == True:
                return d1
    return False

# Trial Test 1
print(addition_puzzle('AND','MAN','COOL'))

