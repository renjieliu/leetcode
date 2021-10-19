class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        arr = [[0],[0]]
        for i, c in enumerate(s):
            if c != s[i-1]:
                arr[int(c)].append(1)
            else:
                arr[int(c)][-1]+=1
        return max(arr[0]) < max(arr[1])

