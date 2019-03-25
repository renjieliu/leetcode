def checkValidString(s: str): # (*))(*()
    if len(s)==0:
        return True

    temp = list(s)
    find = [] #to store the position of the (  find[-1] is the closest for the current )
    minus = 0 #the array will be shifted left for 2 positions everytime a pair is found.
    left = 0 #how many ( has been found
    #1. remove all the regular pair
    for i in range(len(s)):
        #print(temp)
        if s[i]=="(":
            left += 1
            find.append(i+minus)
        elif s[i]== ")":
            if left >0:
                temp = temp[:find[-1]] + temp[find[-1]+1:i+minus] + temp[i+1+minus:]
                left -=1
                minus -=2
                find.pop(-1)

    # 2. treat * as (
    s1 = "".join(temp)
    find = []
    minus = 0
    left = 0
    for i in range(len(s1)):
        #print(temp)
        if s1[i]=="*":
            left += 1
            find.append(i+minus)
        elif s1[i]== ")":
            if left >0:
                temp = temp[:find[-1]] + temp[find[-1]+1:i+minus] + temp[i+1+minus:]
                left -=1
                minus -=2
                find.pop(-1)

        #print(temp)

    #3. treat * as )

    s1 = "".join(temp)
    find = []
    minus = 0
    left = 0
    for i in range(len(s1)):
        if s1[i]=="(":
            left += 1
            find.append(i+minus)

        elif s1[i]== "*":
            if left >0:
                temp = temp[:find[-1]] + temp[find[-1]+1:i+minus] + temp[i+1+minus:]
                left -=1
                minus -=2
                find.pop(-1)

    if temp.count("(") + temp.count(")") ==0:
        return True
    else:
        return False




print(checkValidString("()"))
print(checkValidString("(*)"))
print(checkValidString("(*))"))
print(checkValidString("((*)"))
print(checkValidString("(*))(*()"))
print(checkValidString("((((****"))
print(checkValidString("**)))"))
print(checkValidString("****))))"))
print(checkValidString("((*))")) #true



