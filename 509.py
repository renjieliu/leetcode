def fib( N: 'int'):
    if N==0:
        return 0
    if N == 1 or N == 2:
        return 1
    else:
        list = []
        list.append(1)
        list.append(1)
        for i in range(2, N):
            list.append(list[i - 2] + list[i - 1])

        return list[-1]

print(fib(30))