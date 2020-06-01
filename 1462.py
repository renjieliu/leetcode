class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: 'List[List[int]]', queries: 'List[List[int]]') -> 'List[bool]':
        hmp_dep = {}
        for i, j in prerequisites:  # j is depending on i
            if j not in hmp_dep:
                hmp_dep[j] = []  # all the course j depending on
            hmp_dep[j].append(i)

        def dfs(hmp_dep, c, dp):
            if c not in dp:
                dp[c] = []
            for x in hmp_dep[c]:
                dp[c].append(x)
                if x in hmp_dep:
                    if x in dp:
                        dp[c] += dp[x]
                    else:
                        dfs(hmp_dep, x, dp)
                        dp[c] += dp[x]
            dp[c] = list(set(dp[c]))

        dp = {}
        for i in range(n):
            if i not in hmp_dep:  # current course does not have any prereq
                dp[i] = []
            else:
                if i not in dp:
                    dp[i] = []
                    dfs(hmp_dep, i, dp)

        output = []
        for i, j in queries:
            output.append(False if dp[j] == [] or i not in dp[j] else True)
        return output

