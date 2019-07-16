def relativeSortArray(arr1: 'List[int]', arr2: 'List[int]'):
    output = []
    other = set()
    dict  = {}
    for i in arr1:
        if i not in dict:
            dict[i] = 0
        dict[i]+=1

        if i not in arr2:
            other.add(i)

    for i in arr2:
        output+= [i]*dict[i]

    for i in sorted(list(other)):
        output+= [i] * dict[i]

    return output







print(relativeSortArray( arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31],[2,42,38,0,43,21]))
