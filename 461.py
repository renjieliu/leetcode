def hammingDistance(x, y):
    bin_x = str(bin(x)).replace("0b","")
    bin_y = str(bin(y)).replace("0b","")
    diff = 0

    if len(bin_x)<len(bin_y):
        bin_x  = "0"*(len(bin_y) - len(bin_x)) + bin_x

    if len(bin_y) < len(bin_x):
        bin_y = "0" * (len(bin_x) - len(bin_y)) + bin_y

    for i in range(0, len(bin_x)):
        if bin_x[i] != bin_y[i]:
            diff+=1
    return diff

print(hammingDistance(1,4))






