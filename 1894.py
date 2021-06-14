class Solution:
    def chalkReplacer(self, chalk: 'List[int]', k: int) -> int:
        rem = k % sum(chalk)
        for i in range(len(chalk)):
            if rem - chalk[i] < 0: #if the rem cannot help curr student to finish the task, curr needs to replace the chalk
                return i
            rem -= chalk[i]

