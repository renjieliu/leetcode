class Solution:
    def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: int, t: int) -> bool:
        dis = k
        val = t
        if val < 0 or dis == 0:
            return False
        else:
            bks, total = {}, t + 1
            for i, c in enumerate(nums):
                b = c // total
                if b in bks:
                    return True
                else:
                    bks[b] = c
                    if (b - 1 in bks and abs(c - bks[b - 1]) <= val) or (b + 1 in bks and abs(bks[b + 1] - c) <= val):
                        return True
                    if i >= dis:
                        del bks[nums[i - dis] // total]  # delete the first item from the hash.
            return False

