def findGCD(num1, num2):
    output  = 0
    bigger = num1 if num1>num2 else num2
    smaller = num1 if num2>num1 else num2
    while bigger%smaller != 0:
        t= bigger
        bigger = smaller
        smaller = t%smaller

    return smaller

print (findGCD( 1112, 695))


