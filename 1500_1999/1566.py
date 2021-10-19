class Solution:
    def containsPattern(self, arr: 'List[int]', m: int, k: int) -> bool:
        def compare(arr, m):
            prev = arr[:m]
            temp = []
            for a in arr[m:]:
                temp.append(a)
                if len(temp) == m:
                    if temp == prev:
                        prev = temp
                        temp = []
                    else:
                        return False
            return True

        for i in range(1 if len(arr) - m * k == 0 else len(
                arr) - m * k):  # in case the m*k == len(arr), need to compare at least once
            if compare(arr[i: i + m * k], m) == True: return True
        return False
