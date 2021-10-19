class Solution:
    def maxSumDivThree(self, nums: 'List[int]') -> int:
        mod_dict = {0: [], 1: [], 2: []}
        for n in nums:
            t = n % 3
            mod_dict[t].append(n)
        # for all the mod_dict[0], they can be taken out directly
        output = sum(mod_dict[0]) if len(mod_dict[0]) > 0 else 0
        mod_dict[2].sort(reverse=True)
        mod_dict[1].sort(reverse=True)
        output += (sum(mod_dict[2]) + sum(mod_dict[1]))
        o1 = o2 = output
        o1_pass = o2_pass = 0
        while o1 % 3 != 0:
            if mod_dict[1] == []:
                o1_pass = 1
                break
            else:
                o1 -= mod_dict[1].pop()  # calculate if deduct from mod_1

        while o2 % 3 != 0:
            if mod_dict[2] == []:
                o2_pass = 1
                break
            else:
                o2 -= mod_dict[2].pop()  # calculate if deduct from mod_2

        if o1_pass == 1:
            return o2
        elif o2_pass == 1:
            return o1
        else:
            return max(o1, o2)
