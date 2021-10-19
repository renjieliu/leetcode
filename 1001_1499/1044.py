class Solution:
    def longestDupSubstring(self, S: str) -> str:
        def search(mid, S) -> str:
            total = len(S)
            nums = [ord(S[i]) - ord('a') for i in range(total)]
            a = 26
            mod = 2 ** 64
            currHash = 0
            for i in range(mid):
                currHash = (currHash * a + nums[i]) % mod

            hmp = {currHash}
            constant = a ** mid % mod
            for i in range(1, total - mid + 1):  # computing the rolling hash for s
                currHash = (currHash * a - nums[i - 1] * constant + nums[i + mid - 1]) % mod
                if currHash in hmp:
                    return i
                hmp.add(currHash)
            return -1

        s, e = 0, len(S)
        output = ""
        while s <= e:
            mid = (s + e) // 2
            res = search(mid, S)
            if res != -1:
                output = S[res:res + mid] if len(S[res:res + mid]) > len(output) else output
                s = mid + 1
            else:
                e = mid - 1

        return output