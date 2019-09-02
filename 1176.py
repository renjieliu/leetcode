def dietPlanPerformance(calories: 'List[int]', k: int, lower: int, upper: int):
    check = []
    s = 0
    for i in range(len(calories)):
        s += calories[i]
        check.append(s)

    temp = []

    for i in range(len(check)):
        if i == k - 1:
            temp.append(check[i])
        elif i > k - 1:
            temp.append(check[i] - check[i - k])

    output = 0

    for i in temp:
        if i < lower:
            output -= 1
        elif i > upper:
            output += 1
    return output



#Revised version, combine the last part with the second part when generating the sum array (here named as temp)
    # check = []
    # s = 0
    # for i in range(len(calories)):
    #     s+=calories[i]
    #     check.append(s)
    #
    # #temp = []
    # output = 0
    # curr = 0
    # for i in range(len(check)):
    #     if i == k-1:
    #         curr = check[i]
    #     elif i>k-1:
    #         curr = check[i] - check[i-k]
    #     else:
    #         curr = float('inf')
    #
    #     if curr != float('inf'):
    #         if curr < lower:
    #             output -= 1
    #         elif curr > upper:
    #             output +=1
    #
    # #
    # #
    # #
    # # for i in temp:
    # #     if i<lower:
    # #         output-=1
    # #     elif i>upper:
    # #         output +=1
    # return output


print(dietPlanPerformance(calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3)) #0
print(dietPlanPerformance(calories = [3,2], k = 2, lower = 0, upper = 1)) #1
print(dietPlanPerformance(calories = [6,5,0,0], k = 2, lower = 1, upper = 5)) #0
