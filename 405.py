def toBinComp(n):
    temp = abs(n)
    output = ""
    while temp > 0:
        #output = str(temp%2) + output #get the ~num in binary form
        output = str(abs(1-(temp%2))) + output #get the ~num in binary form
        temp//=2


    output = str(1)*(32 - len(output)) + output
    found = 0

    #below is to plus 1
    for i in range(len(output)-1, -1, -1):
        if output[i] == "0":
            found = 1
            return output[0:i] + str(1) + str(0) * len(output[i+1:])

    if found ==0 :
        return str(1) + str(0) * len(output)



def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    map = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    output =  ""
    if num ==0:
        return 0

    elif num>0:
        n = num
        while n >0:
            output = ( map[n%16] if n%16 in map else str(n%16) )  + output
            n=n//16
        return output

    else:
        dict =  {
                '0000': '0',
                '0001':	'1',
                '0010':	'2',
                '0011':	'3',
                '0100':	'4',
                '0101':	'5',
                '0110':	'6',
                '0111':	'7',
                '1000':	'8',
                '1001':	'9',
                '1010': 'a',
                '1011': 'b',
                '1100': 'c',
                '1101': 'd',
                '1110': 'e',
                '1111': 'f'
             }

        output  = ""
        t = toBinComp(num)
        for i in range(0,len(t),4):
            output+=dict[t[i:i+4]]
        return output

# print(toHex(-8)) #"fffffff8"
#
# print(toHex(1000)) #"3e8"

print(toHex(-100000)) #"fffe7960"




