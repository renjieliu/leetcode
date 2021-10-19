def binaryGap(N: 'int'):
    b = str(bin(N))[2:]
    m = 0
    found = 0
    curr = 0
    for i in range (0, len(b)):
        if int(b[i]) == 1 and found != 1: #first 1
            found = 1
            curr = i
        elif int(b[i]) == 1 and found == 1:  # it's found before , now compare the index distance
            if i - curr > m:
                m = i-curr

            curr = i


    return m

print(binaryGap(22))
print(binaryGap(5))
print(binaryGap(6))
print(binaryGap(213412311))


