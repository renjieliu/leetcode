def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    x = chars[:]

    chars.clear()
    if len(x)==0:
        return 0
    else:
        output = []
        cnt = 1
        for i in range(1, len(x)):
            if x[i]==x[i-1]:
                cnt+=1
            else:
                output.append(x[i - 1])
                if cnt != 1 :
                    output.append(cnt)
                cnt = 1

        output.append(x[-1])

        if cnt != 1:
            output.append(cnt)

        temp = ""

        for i in output:
            temp+= str(i)

        for i in temp:
            chars.append(i)


        return len(temp)




print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
print(compress(["a", "a", "b"]))

