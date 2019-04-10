def sortArrayByParityII(A: 'List[int]'):
    odd = []
    even = []
    output =[]
    for i in A :
        if i &1==0:
            even.append(i)
        else:
            odd.append(i)
    for i in range(len(A)):
        if i &1==0:
            output.append(even.pop())
        else:
            output.append(odd.pop())

    return output







print(sortArrayByParityII([4,2,5,7]))
