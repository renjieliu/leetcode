class Solution:
    def numPairsDivisibleBy60(self, time: 'List[int]') -> int:
        arr = [_ % 60 for _ in time]
        hmp = {} # each remainder is a stack, to check if the number can find a match in the hashmap
        for i in range(len(arr)):
            a = arr[i]
            if a not in hmp:
                hmp[a] = []
            hmp[a].append(i)

        cnt = 0

        for i, a in enumerate(arr):
            rem = (60 - a) % 60
            if rem in hmp:
                while hmp[rem] and hmp[rem][0] <= i:#pop the stack, until the position is > the current
                    hmp[rem].pop(0)
                cnt += len(hmp[rem])
            # print(hmp)
        return cnt
