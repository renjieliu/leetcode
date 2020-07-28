class Solution:
    def leastInterval(self, tasks: 'List[str]', n: int) -> int:
        if n == 0: return len(tasks)
        hmp = {}
        for t in tasks:
            if t not in hmp: hmp[t] = 0
            hmp[t] += 1
        stk = sorted(list(hmp.values()), reverse=True)
        output = ""
        while stk:  # find next available task, if reach the end,then put 0.
            i = 0
            while i < n + 1:
                stk[i] -= 1
                output += "1"
                i += 1
                if i == len(stk):
                    output += (n + 1 - i) * "0"
                    break
            stk.sort(reverse=True)  # take out the tasks that has been exhausted.
            while stk and stk[-1] == 0:
                stk.pop()

        return len(output.rstrip('0'))  # take out the last 0s, they are not necessary




