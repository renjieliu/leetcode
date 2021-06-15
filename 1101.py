class Solution:
    def earliestAcq(self, logs: 'List[List[int]]', n: int) -> int:
        root = [_ for _ in range(n)]
        logs.sort(key=lambda x: x[0])
        zero = 1  # how many people with zero as root
        for time, f1, f2 in logs:
            if root[f1] != root[f2]:  # check the root of current person
                new = min(root[f1], root[f2])
                old = max(root[f1], root[f2])
                for i in range(n):  # merge the larger number to the smaller number
                    if root[i] == old:
                        root[i] = new
                        if root[i] == 0:
                            zero += 1
            if zero == n:  # all the numbers' root are changed to 0
                return time
            # print(logs, zero, root)
        return -1


