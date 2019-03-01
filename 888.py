def fairCandySwap(A: 'List[int]', B: 'List[int]'):
    sum_A = 0
    sum_B = 0
    for i in A:
        sum_A += i
    for i in B:
        sum_B += i

    dict = []

    for i in A:
        dict.append(i - (sum_A - sum_B) / 2)

    for i in B:
        if i in dict:
            return [int(i + ((sum_A - sum_B) / 2)), i]


print(fairCandySwap([1, 1], [2, 2]))
print(fairCandySwap([1, 2], [2, 3]))
print(fairCandySwap([2], [1, 3]))
print(fairCandySwap([1, 2, 5], [2, 4]))
