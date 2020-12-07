class Solution:
    def maxOperations(self, nums: 'List[int]', k: int) -> int:
        hmp = {}
        for n in nums:
            if n not in hmp:
                hmp[n] = 0
            hmp[n] += 1
        output = 0
        for n in nums:
            if n in hmp:
                if k - n in hmp:
                    if n == k - n:  # if the rem is the same as n , the same number needs to be taken out twice
                        if hmp[n] >= 2:
                            hmp[n] -= 2
                            output += 1
                            if hmp[n] <= 0:
                                del hmp[n]
                    else:
                        hmp[n] -= 1
                        hmp[k - n] -= 1
                        output += 1
                        if hmp[n] <= 0:
                            del hmp[n]
                        if hmp[k - n] <= 0:
                            del hmp[k - n]

        return output








