class Solution: #RL 20210829: Copied solution
    def minPatches(self, nums, n):
        def merge(intervals):
            intervals.sort(key=lambda x: x[0])
            merged = []

            for interval in intervals:
                if not merged or merged[-1][1] < interval[0] - 1:
                    merged.append(interval)
                else:
                    merged[-1][1] = max(merged[-1][1], interval[1])

            return merged

        ints, patches = [[0, 0]], 0
        for num in nums:
            ints = merge(ints + [[i + num, j + num] for i, j in ints])

        while ints[0][1] < n:
            ints = merge(ints + [[i + ints[0][1] + 1, j + ints[0][1] + 1] for i, j in ints])
            patches += 1

        return patches








