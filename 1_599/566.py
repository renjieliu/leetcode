def matrixReshape(nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    temp = []
    output = [[]]
    for i in nums:
        for j in i:
            temp.append(j)

    if r*c != len(temp):
        return nums

    else:
        e = 0
        cnt = 0
        now = 0
        for i in temp:
            cnt += 1
            now += 1
            if now > len(temp):
                return output
            elif cnt <= c:
                output[e].append(i)
            elif cnt > c :
                output.append([])
                e+=1
                output[e].append(i)
                cnt = 1


    return output

print( matrixReshape([[1,2,3,4,5,6,7,8,9,10], [11,2]],4,3))

