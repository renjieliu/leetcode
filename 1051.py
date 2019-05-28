def heightChecker(heights: 'List[int]'):
    compare = sorted(heights)
    cnt = 0
    for i in range(len(heights)):
        if heights[i] != compare[i]:
            cnt+=1

    return cnt

print(heightChecker([1,1,4,2,1,3]))




