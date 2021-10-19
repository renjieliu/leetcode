def say(input):
    ini = input[0]
    output = ""
    cnt = 1
    for i in range(1, len(input)):
        if input[i]== input[i-1]:
            cnt +=1
        else:
            output+=str(cnt)+ str(input[i-1])
            cnt = 1

    output += str(cnt) + str(input[i])

    return output



def countAndSay(n: int):
    if n == 1 :
        return "1"
    elif n ==2:
        return "11"

    curr = "11"
    for i in range(3,n+1):
        curr = say(curr)
    return curr

print(countAndSay(1))
print(countAndSay(2))
print(countAndSay(3))
print(countAndSay(4))
print(countAndSay(5))
print(countAndSay(6))
print(countAndSay(30))



