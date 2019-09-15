def maxNumberOfBalloons(text: str):
    dict  = {}
    for i in text:
        if i not in dict:
            dict[i] = 0
        dict[i] +=1

    if 'b' not in dict or 'a' not in dict or'l' not in dict or'o' not in dict or 'n' not in dict:
        return 0

    else:
        dict['l'] //=2
        dict['o'] //=2
        output = float('inf')
        for k,v in dict.items():
            if k in "balloon":
                output= min(output, v)

    return output

print(maxNumberOfBalloons(text = "nlaebolko"))
print(maxNumberOfBalloons(text = "loonbalxballpoon"))
print(maxNumberOfBalloons(text = "leetcode"))

