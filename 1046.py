def lastStoneWeight(stones: 'List[int]'):
    S = list(stones.copy())
    while len(S)>1:
        S.sort()
        a = S[-1]
        b = S[-2]
        #a >=b
        S.pop()
        S.pop()
        if a==b:
            pass
        else:
            S.append(a-b)

    return S[0] if len(S) >0 else 0

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([2,2]))
