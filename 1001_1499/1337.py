class Solution:
    def kWeakestRows(self, mat: 'List[List[int]]', k: int) -> 'List[int]':
        arr = []
        for i in range(len(mat)):
            curr = 0
            arr.append([i])
            for c in mat[i]:
                if c == 1:
                    curr+=c
                else:
                    break
            arr[-1].append(curr)
        arr.sort(key = lambda x: [x[1], x[0]])
        output = []
        #print(arr)
        for i in range(k):
            output.append(arr[i][0])
        return output
