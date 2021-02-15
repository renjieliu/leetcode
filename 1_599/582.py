class Solution:
    def killProcess(self, pid: 'List[int]', ppid: 'List[int]', kill: int) -> 'List[int]':
        prc = {}
        for i, p in enumerate(ppid):
            if p not in prc:
                prc[p] = []
            prc[p].append(pid[i])
        # print(prc)
        output = [kill]
        if kill not in prc: #it does not have a child process.
            return output
        else:
            stk = prc[kill] #first layer processes mapped to kill
            del prc[kill]
            while stk: #BFS to keep finding the child processes to kill
                nxt = []
                while stk:
                    child = stk.pop(0)
                    output.append(child)
                    if child in prc:
                        nxt += prc[child]
                        del prc[child]
                stk = nxt


            return output

#previous DFS approach
# class Solution:
#     def killProcess(self, pid: 'List[int]', ppid: 'List[int]', kill: int) -> 'List[int]':
#         def dfs(curr, child, output):  # to find child
#             if curr not in child:
#                 return None
#             for c in child[curr]:
#                 output.append(c)
#                 dfs(c, child, output)
#
#         child = {}
#         for i in range(len(ppid)):
#             if ppid[i] not in child:
#                 child[ppid[i]] = []
#             child[ppid[i]].append(pid[i])
#
#         output = [kill]
#         dfs(kill, child, output)
#         return output