def dailyTemperatures(T: 'List[int]'):
    curr_greater = []
    output = [0]*len(T)
    for i in range(len(T)-1, -1, -1):
        while len(curr_greater)!=0 and T[curr_greater[-1]]<=T[i]:
            curr_greater.pop()
        if len(curr_greater)!=0:
            output[i] = curr_greater[-1] - i
        curr_greater.append(i)

    return output

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))