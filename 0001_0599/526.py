class Solution:
    def countArrangement(self, n: int) -> int:
        self.cnt = 0

        def swap(arr, a, b):
            t = arr[a]
            arr[a] = arr[b]
            arr[b] = t

        def perm(arr, loc):
            if loc == len(arr):
                self.cnt += 1
            for i in range(loc, len(arr)):
                swap(arr, i, loc)  # swap it with itself first, to make sure the current combination is counted

                if arr[loc] % (loc + 1) == 0 or (loc + 1) % arr[loc] == 0:
                    perm(arr, loc + 1)

                swap(arr, i, loc)

        perm([_ for _ in range(1, n + 1)], 0)

        return self.cnt
