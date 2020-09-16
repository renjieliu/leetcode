class Solution:
    def findMaximumXOR(self, nums: 'List[int]') -> int:
        if len(nums) < 2:
            return 0
        else:
            def lkp(arr, curr, pre, lkp_set):  # to find if pre-length of arr element ^ curr is in the lkp_set
                for a in arr:
                    temp = ""
                    for i, c in enumerate(a[:pre]):
                        temp += "1" if c != curr[i] else "0"
                    if temp in lkp_set:
                        return 1
                return 0

            maxBits = len(bin(max(nums)).replace('0b', ''))  # maxBits
            toBin = lambda x: bin(x).replace('0b', '')
            arr = ['0' * (maxBits - len(toBin(n))) + toBin(n) for n in nums]  # turn to 0
            output = ""
            for i in range(maxBits):
                curr = output + "1"  # assume it can find n^curr in the array, else it will be 0
                lkp_set = {n[:i + 1] for n in arr}
                # print(lkp_set)
                if lkp(arr, curr, i + 1, lkp_set) == 1:
                    output += "1"
                else:
                    output += "0"

            return int(output, 2)

