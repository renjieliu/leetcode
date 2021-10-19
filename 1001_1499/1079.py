class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def helper(output, arr, curr, target):
            if len(curr) == target:
                output.append(curr)
            else:
                for i in range(len(arr)):
                    helper(output, arr[:i] + arr[i + 1:], curr + [arr[i]], target)

        output = []
        arr = [_ for _ in range(1, len(tiles) + 1)]
        for i in range(1, len(tiles) + 1):
            helper(output, arr, [], i)
        ans = set()
        for o in output:
            curr = ""
            for c in o:
                curr += tiles[c - 1]
            if curr not in ans:
                ans.add(curr)
        return len(ans)
