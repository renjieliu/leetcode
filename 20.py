def isValid(s: str):
    if len(s) ==0:
        return True
    map  = {}
    c = 0
    for i in s:
        if i =="{":
            if "{" not in map:
                map["{"] = []
            map["{"].append(c)

        elif i == "[":
            if "[" not in map:
                map["["] = []
            map["["].append(c)

        elif i == "(":
            if "(" not in map:
                map["("] = []
            map["("].append(c)

        elif i == "}":
            if "{" not in map or len(map["{"])<1 or c - map["{"][-1] >1 :
                return False
            else:
                map["{"].pop()
                c -= 2 #once found, backtrack the current pointer by 2 position.

        elif i == "]":
            if "[" not in map or len(map["["])<1 or c - map["["][-1] >1 :
                return False
            else:
                map["["].pop()
                c -= 2

        elif i == ")":
            if "(" not in map or len(map["("]) < 1 or c - map["("][-1] >1 :
                return False
            else:
                map["("].pop()
                c-=2

        c+=1

    summ = 0
    for v in map.values():
        summ+=len(v)
    if summ !=0 :
        return False
    else:
        return True


print(isValid( "()"))
print(isValid( "()[]{}"))
print(isValid( "(]"))
print(isValid( "([)]"))
print(isValid( "{[]}"))