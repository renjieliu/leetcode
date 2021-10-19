class Solution:
    def minimumSemesters(self, n: int, relations: 'List[List[int]]') -> int:
        pre_course = {}
        advance_course = set() # courses cannot be learned first
        for pre, c in relations:
            advance_course.add(c)
            if pre not in pre_course:
                pre_course[pre] = []
            pre_course[pre].append(c)

        def layers(dp, layer, c, pre_course, seen): #for each root course, find the deepest layer count
            if dp[c] != 0:
                return dp[c]
            else:
                if c not in pre_course: #reach the end, current course takes 1 semester to finish
                    dp[c] = 1
                    return dp[c]
                else:
                    for nxt in pre_course[c]:
                        if nxt in seen:
                            dp[c] = -1
                        else:
                            seen.add(nxt)
                            t = layers(dp, layer+1, nxt, pre_course, seen)
                            if t == -1:
                                dp[c] = -1
                                return dp[c]
                            else:
                                dp[c] = max(dp[c], 1+t)
                            seen.remove(nxt)
                    return dp[c]

        root = list(set([_ for _ in range(1,n+1)]) - advance_course)
        if root == []: # all the courses need a pre
            return -1
        else:
            dp = [0] * (n+1)
            for r in root:
                t = layers(dp, 1, r, pre_course, set())
                if t == -1:
                    return -1
            return max(dp)
              
        