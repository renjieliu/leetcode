class Solution:
    def killProcess(self, pid: 'List[int]', ppid: 'List[int]', kill: int) -> 'List[int]':
        def dfs(curr, child, output):  # to find child
            if curr not in child:
                return None
            for c in child[curr]:
                output.append(c)
                dfs(c, child, output)

        child = {}
        for i in range(len(ppid)):
            if ppid[i] not in child:
                child[ppid[i]] = []
            child[ppid[i]].append(pid[i])

        output = [kill]
        dfs(kill, child, output)
        return output