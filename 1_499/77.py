class Solution:
    def combine(self, n: int, k: int) -> 'List[List[int]]':
        def dfs(output, k, curr, rest):
            if len(curr) == k:
                output.append(curr)
                return -1
            else:
                for i in range(len(rest)):
                    t = curr + [rest[i]]
                    dfs(output, k, t, rest[i + 1:])

        if k == 0:
            return [[]]
        output = []
        rest = [_ for _ in range(1, n + 1)]
        for i in range(len(rest)):
            dfs(output, k, [rest[i]], rest[i + 1:])
        return output