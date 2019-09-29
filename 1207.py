def uniqueOccurrences(arr: 'List[int]') :
    dict_1 = {}
    for i in arr:
        if i not in dict_1:
            dict_1[i] = 0
        dict_1[i]+=1


    dict_2 = {}
    for v in dict_1.values():
        if v not in dict_2:
            dict_2[v] = 1
        else:
            return False

    return True


print(uniqueOccurrences( [1,2,2,1,1,3]))
print(uniqueOccurrences( [1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
