def bitwiseComplement(N: int):
    t = str(bin(N)).replace('0b','')
    output  = 0
    temp = ""
    for i in t:
        temp += str(abs(int(i)-1))

    cnt = 0
    for k in temp[::-1]:
        output += int(k)*(2**cnt)
        cnt+=1

    return output




print(bitwiseComplement(7))
print(bitwiseComplement(5))
print(bitwiseComplement(10))
print(bitwiseComplement(0))