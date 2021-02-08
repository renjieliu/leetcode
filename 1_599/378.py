def kthSmallest(matrix: 'List[List[int]]', k: int):
    arr = []
    for i in matrix:
        arr += i

    arr.sort()
    return arr[k-1]

print(kthSmallest( [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8))
