class Solution:
    def maximumRemovals(self, s: str, p: str, removable: 'List[int]') -> int:
        def isSub(arr_1, arr_2, arr):
            # print(arr_1, arr_2, arr)
            for a in arr:
                arr_1[a] = ""
            cnt = 0
            total = len(arr_2)
            while arr_1 and arr_2:
                if arr_1[0] == arr_2[0]:
                    cnt += 1
                    arr_1.popleft()
                    arr_2.popleft()
                else:
                    arr_1.popleft()
            return cnt == total

        st = 0
        end = len(removable) - 1
        output = -1  # incase cannot remove anything, output +1 = 0, 0 will be returned
        while st <= end:  # binary search to check all the possibilities
            mid = st - (st - end) // 2
            if isSub(deque(s), deque(p), removable[:mid + 1]):
                output = mid  # index, cnt = index+1, as returnd
                st = mid + 1
            else:
                end = mid - 1

        return output + 1

