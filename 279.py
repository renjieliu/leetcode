def numSquares(n: int) -> int:
    arr = [float('inf')] * (n + 1)
    arr[0] = 0

    for i in range(1, n+1):
        arr[i] = min(arr[i-j*j] for j in range(1, int(i**0.5)+1)) + 1

    return arr[n]


print(numSquares(12))
print(numSquares(4781))
print(numSquares(47814))
print(numSquares(7927))




