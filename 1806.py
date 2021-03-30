class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [_ for _ in range(n)]
        arr = []
        for i in range(n):
            arr.append(perm[i//2] if i%2 ==0 else perm[n // 2 + (i - 1) // 2] )
        cnt = 1
        while arr != perm:
            temp = []
            for i in range(n):
                temp.append(arr[i//2] if i%2 ==0 else arr[n // 2 + (i - 1) // 2] )
            arr = temp
            cnt += 1
        return cnt
