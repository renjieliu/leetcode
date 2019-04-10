def sortArrayByParityII(A: 'List[int]'):
    output = [None] * len(A)
    curr_odd = 1
    curr_even = 0
    for i in A:
        if i&1==0:
            output[curr_even] = i
            curr_even+=2
        else:
            output[curr_odd] = i
            curr_odd += 2

    return output


    #
    #
    # odd = []
    # even = []
    # output =[]
    # for i in A :
    #     if i &1==0:
    #         even.append(i)
    #     else:
    #         odd.append(i)
    # for i in range(len(A)):
    #     if i &1==0:
    #         output.append(even.pop())
    #     else:
    #         output.append(odd.pop())
    #
    # return output
    #






print(sortArrayByParityII([4,2,5,7]))
