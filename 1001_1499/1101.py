class Solution:
    def earliestAcq(self, logs: 'List[List[int]]', n: int) -> int:
        def find(root, v):
            if root[v] != v:
                root[v] = find(root, root[v])
            return root[v]
        
        def union(root, a, b, group_zero): #add to the smaller number
            r_a = find(root, a)
            r_b = find(root, b)
            A = min(r_a, r_b)
            B = max(r_a, r_b)
            root[B] = A
            if A == 0:
                group_zero.add(B)
            for i in range(len(root)):
                if root[i] == B:
                    root[i] = A
                    if A == 0:
                        group_zero.add(i)

        root = [_ for _ in range(n)]
        group_zero = {0} #initially, it contains itself
        logs.sort(key = lambda x : x[0])
        
        for t, a, b in logs: #every one should be added to the group of 0
            union(root, a, b, group_zero)
            if len(group_zero) == n:
                return t 
            # print(root, t, group_zero)   
        return -1
            


# previous approach

# class Solution:
#     def earliestAcq(self, logs: 'List[List[int]]', n: int) -> int:
#         def find(root, v):  # to find the root of v.. if current number != v, then current is a pointer
#             if v != root[v]:
#                 root[v] = find(root, root[v])
#             return root[v]

#         def union(root, a, b):  # put any one to another tree
#             root[a] = b

#         group = n  # initially, there are n people, so it's n groups
#         logs.sort(key=lambda x: x[0])
#         root = [_ for _ in range(n)]
#         for time, a, b in logs:
#             x = find(root, a)
#             y = find(root, b)
#             if x != y:
#                 group -= 1  # 2 people becomes 1, need to reduce total group by1
#                 union(root, x, y)
#             if group == 1:
#                 return time
#         return -1

# previous approach
# class Solution:
#     def earliestAcq(self, logs: 'List[List[int]]', n: int) -> int:
#         root = [_ for _ in range(n)]
#         logs.sort(key=lambda x: x[0])
#         zero = 1  # how many people with zero as root
#         for time, f1, f2 in logs:
#             if root[f1] != root[f2]:  # check the root of current person
#                 new = min(root[f1], root[f2])
#                 old = max(root[f1], root[f2])
#                 for i in range(n):  # merge the larger number to the smaller number
#                     if root[i] == old:
#                         root[i] = new
#                         if root[i] == 0:
#                             zero += 1
#             if zero == n:  # all the numbers' root are changed to 0
#                 return time
#             # print(logs, zero, root)
#         return -1


