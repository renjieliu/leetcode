class Solution:
    def mostVisited(self, n: int, rounds: 'List[int]') -> 'List[int]':
        def path(s, e,
                 total):  # get path of each round, excluding end, it's also the start for the next round, avoid double counting
            if e > s:
                return list(range(s, e))
            else:
                return list(range(s, total + 1)) + list(range(1, e))

        arr = [-1] + [0] * n
        for i in range(len(rounds) - 1):  # add the sectors to the arr.
            res = path(rounds[i], rounds[i + 1] + (1 if i == len(rounds) - 2 else 0),
                       n)  # count the end if it's the last round
            # print(res)
            for x in res:
                arr[x] += 1
        # print(arr)
        m = max(arr)
        output = []
        for i, c in enumerate(arr):
            if c == m:
                output.append(i)
        output.sort()
        return output
