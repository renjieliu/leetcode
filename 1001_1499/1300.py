class Solution:
    def findBestValue(self, arr: 'List[int]', target: int) -> int:
        s = sum(arr)  # find how many numbers are greater than the current ones
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = [0, 0]  # [how many current numbers, how many greater than curr]
            hmp[a][0] += 1
        k = sorted(hmp.keys(), reverse=1)
        t = 0
        for i in range(len(k)):
            hmp[k[i]][1] = t
            t += hmp[k[i]][0]

        if s <= target:
            return k[0]  # return the max one in the array, no need to trim the numbers
        else:  # if s > target, need to decrease the highest numbers
            curr = k[0]
            prev_s = s
            deduction = 0  # how much to be deducted from the sum
            while True:
                s -= deduction
                if s <= target:
                    return curr + 1 if abs(target - prev_s) < abs(target - s) else curr  # prev number is curr+1.
                if curr in hmp:
                    deduction = hmp[curr][1] + hmp[curr][0]
                prev_s = s
                curr -= 1

            return 0

