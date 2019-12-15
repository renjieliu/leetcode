class Solution:
    def removeCoveredIntervals(self, intervals: 'List[List[int]]') -> int:
        def dfs(check, start, cnt, rng, intervals):
            if check[start] != 0:  # it has been checked before
                return -1
            else:
                check[start] = cnt
                curr = start + 1
                while curr < len(intervals):
                    A = rng
                    B = intervals[curr]
                    if intervals[curr][0] > rng[1]:
                        return 0
                    elif (B[0] <= A[0] <= A[1] <= B[1]) or (
                            A[0] <= B[0] <= B[1] <= A[1]):  # B within A or A within B
                        a = intervals[curr][1] - intervals[curr][0]
                        b = rng[1] - rng[0]
                        currRng = intervals[curr] if a > b else rng  # to get the larger range for checking
                        if dfs(check, curr, cnt, currRng, intervals) == 0:
                            break
                    curr += 1

                return 0

        intervals.sort()
        check = [0] * len(intervals)
        cnt = 0
        for i in range(len(intervals)):
            if check[i] == 0:
                cnt += 1
                rng = intervals[i]  # the range to check
                dfs(check, i, cnt, rng, intervals)
        return cnt