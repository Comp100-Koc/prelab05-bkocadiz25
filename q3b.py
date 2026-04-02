def add_binary(a, b):
    '''
    Given two strings perform binary addition and return the result as a string
    '''
    numA = a.split("b")[1]
    numB = b.split("b")[1]
    
    if len(numA) < len(numB):
        numA = (len(numB) - len(numA))*"0" + numA
    elif len(numB) < len(numA):
        numB = (len(numA) - len(numB))*"0" + numB
    
    c = "0"
    
    A = numA[::-1]
    B = numB[::-1]
    tot = ""
    
    for i in range(len(numB)):
        if A[i] == "0" and B[i] == "0":
            tot += c
            c = "0"
        elif (A[i] == "0" and B[i] == "1") or (B[i] == "0" and A[i] == "1"):
            if c == "0":
                tot += "1"
                c = "0"
            elif c == "1":
                tot += "0"
                c = "1"
        elif A[i] == "1" and B[i] == "1":
            if c == "0":
                tot += "0"
                c = "1"
            elif c == "1":
                tot += "1"
                c = "1"
    if c == "1":
        tot += "1"
    
    result = tot[::-1].lstrip("0")
    if result == "":
        result = "0"
            
    return "0b" + result