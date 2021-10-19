import random;


class Solution:

    def __init__(self, w: 'List[int]'):
        self.stk = [w[0]]
        for i in w[1:]:
            self.stk.append(self.stk[-1] + i)  # the weight up to now

    def pickIndex(self) -> int:
        w = random.randint(1, self.stk[-1])  # pick up a random number

        def binSearch(arr, target):  # find which index will contain the target weight
            s = 0
            e = len(arr) - 1
            while s <= e:
                mid = (s + e) // 2
                if arr[mid] == target:
                    return mid
                else:
                    if arr[mid] > target:
                        e = mid - 1
                    else:
                        s = mid + 1
            return s

        return binSearch(self.stk, w)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()