def maxProfitAssignment(difficulty: 'List[int]', profit: 'List[int]', worker: 'List[int]'):
    worker.sort()
    lkp = []
    for d in range(len(difficulty)):
        lkp.append([ difficulty[d], profit[d] ])
    ref = sorted(lkp, key=lambda x: x[0])

    m = ref[-1][0]
    prof_arr = [0] * (m+1) #the array for the max profit the worker can get.

    pos = ref[0][0]
    prof_arr[pos] = ref[0][1]
    curr_max = prof_arr[pos]
    for i in range(1, len(ref)):
        while pos <ref[i][0]:
            prof_arr[pos] = curr_max
            pos+=1
        curr_max = max(curr_max, ref[i][1])

    prof_arr[ref[-1][0]] = curr_max #the last element will not be poulated in the above iteration

    output = 0
    for i in worker:
        if i > ref[-1][0]:
            output+= prof_arr[-1]
        else:
            output += prof_arr[i]


    return output


print(maxProfitAssignment(difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]))
print(maxProfitAssignment([68, 35, 52, 47, 86],
                          [67, 17, 1, 81, 3],
                          [92, 10, 85, 84, 82]))  # 324




