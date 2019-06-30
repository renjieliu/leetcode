import math

def pathInZigZagTree(label: int):
    lines = int(math.log(label)/math.log(2)) + 1
    map_num = {}
    for i in range(lines+1):
        map_num[i] = []
        for j in range(int(2**(i-1)),2**i):
            map_num[i].append(j)

        if i%2 ==0:
            map_num[i] =  map_num[i][::-1]

    curr = map_num[lines].index(label)
    output = [label]
    for i in range(lines-1, 0, -1):
        curr = curr//2
        output.append(map_num[i][curr])


    return output[::-1]



print(pathInZigZagTree(26))
print(pathInZigZagTree(14))