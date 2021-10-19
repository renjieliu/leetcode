def buildString(pattern):
    pick = ['1', '2']
    output = '1'
    pos = 1
    for i in range(1, len(pattern)):
        output += pick[pos%2] * int(pattern[i])
        pos+=1

    return output

def magicalString(n: int):
    if n in [1,2,3]:
        return 1

    temp = '122'
    while len(temp)<n:
        temp = buildString(temp)

    return len(temp[:n]) - len(temp[:n].replace('1',''))

print(magicalString(100000))
print(magicalString(0))
print(magicalString(1))