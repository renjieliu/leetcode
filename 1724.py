class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: 'List[List[int]]'):
        graph = collections.defaultdict(lambda: float("inf"))
        for u, v, dis in edgeList:
            u, v = min(u, v), max(u, v)
            graph[u, v] = min(graph[u, v], dis)
        edges_pq = [(dis, u, v) for (u, v), dis in graph.items()]
        heapq.heapify(edges_pq)
        self.edges_pq = edges_pq
        self.weights = [1 for _ in range(n)]
        self.parents = list(range(n))
        self.distances = [0 for _ in range(n)]

    def _get_root(self, node, limit):
        if self.parents[node] != node and self.distances[node] < limit:
            return self._get_root(self.parents[node], limit)
        return node

    def _union(self, node1, node2, distance):
        root1 = self._get_root(node1, distance+1)
        root2 = self._get_root(node2, distance+1)
        if root1 == root2:
            return False

        if self.weights[root1] >= self.weights[root2]:
            self.distances[root2] = distance
            self.parents[root2] = root1
            self.weights[root1] += self.weights[root2]
        else:
            self.distances[root1] = distance
            self.parents[root1] = root2
            self.weights[root2] += self.weights[root1]
        return True

    def query(self, p: int, q: int, limit: int) -> bool:
        root_p = self._get_root(p, limit)
        root_q = self._get_root(q, limit)

        while root_p != root_q and self.edges_pq and self.edges_pq[0][0] < limit:
            dis, u, v = heapq.heappop(self.edges_pq)  # lazy pop
            self._union(u, v, dis)

            root_p = self._get_root(root_p, limit)
            root_q = self._get_root(root_q, limit)
        return root_p == root_q


# my approach: TLE

# class DistanceLimitedPathsExist: #form a tree, and use dijkstra's algo to check if limited path exists

#     def find(self, root, v):
#         if v!=root[v]:
#             root[v] = self.find(root, root[v])
#         return root[v]

#     def union(self, root, size,a, b):
#         root_a = self.find(root, a)
#         root_b = self.find(root, b)
#         if size[root_a] >= size[root_b]:
#             root[root_b] = self.find(root, a)
#             size[root_a] += size[root_b]
#         else:
#             root[root_a] = self.find(root, b)
#             size[root_b] += size[root_a]

#         # if (a,b) == (470,1951):
#         #     print(root[a], root[b])



#     def __init__(self, n: int, edgeList: List[List[int]]):
#         self.root = [_ for _ in range(n)]
#         self.size = [1 for _ in range(n)]
#         self.neib = {}
#         self.hmp = {}

#         for a, b, dist in edgeList: #build the neibour nodes list and build the tree
#             x = min(a, b)
#             y = max(a, b)
#             if (x,y) not in self.hmp:
#                 self.hmp[(x,y)] = float('inf')
#             self.hmp[(x,y)] = min(self.hmp[(x,y)], dist)

#             root_a = self.find(self.root,x)
#             root_b = self.find(self.root,y)

#             if root_a != root_b:
#                 self.union(self.root, self.size, x, y)

#         for (a, b), cost in self.hmp.items():
#             if a not in self.neib:
#                 self.neib[a] = []
#             if b not in self.neib:
#                 self.neib[b] = []
#             self.neib[a].append([cost, b])
#             self.neib[b].append([cost, a])

#     def query(self, p: int, q: int, limit: int) -> bool:
#         def dij(neib, root, p, q): #using dijkstra's algo to check the if maxCost is < limit
#             if self.find(root, p)!=self.find(root, q) or p not in neib or q not in neib:
#                 return float('inf')
#             else:
#                 pq = [[0, p]] #neib[p][:]
#                 heapq.heapify(pq)
#                 seen = set()
#                 while pq:
#                     maxCost, node = heapq.heappop(pq)
#                     # print('node:', node, 'cost:', maxCost)
#                     if maxCost >=limit:
#                         return float('inf')
#                     elif node == q:
#                         return maxCost
#                     elif node in neib:
#                         for nxtCost, nxtNode in neib[node]:
#                             if (node, nxtNode) not in seen:
#                                 seen.add((node, nxtNode))
#                                 heapq.heappush(pq, [max(maxCost, nxtCost),  nxtNode])


#         t = dij(self.neib, self.root, p, q)
#         return t < limit












# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)