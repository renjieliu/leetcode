class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def perm(nums, N, curr, output, stop):
            if len(curr) == N:
                output.append(curr)
                if len(curr) == stop:
                    return -1
            else:
                for i in range(len(nums)):
                    if perm(nums[:i]+nums[i+1:], N, curr + [nums[i]], output, stop) ==-1:
                        break
        nums = [_ for _ in range(1, n+1)]
        fact = lambda x : 1 if x in [0, 1] else x*fact(x-1)
        ceiling = lambda x: int(x) if x == int(x) else int(x+1)
        start = ceiling(k / (fact(n) // n))  #check start from which number
        stop = k - (start-1) * (fact(n) // n)
        output= []
        perm(nums[:start-1] + nums[start:], n, [start], output, stop)
        return ''.join (map(lambda x : str(x), output[stop-1]))