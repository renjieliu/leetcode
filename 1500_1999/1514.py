class Solution:
    def maxProbability(self, n: int, edges: 'List[List[int]]', succProb: 'List[float]', start: int, end: int) -> float:
        hmp = {}
        for i, p in enumerate(edges):
            if p[0] not in hmp:
                hmp[p[0]] = []  # [node, prob]
            hmp[p[0]].append([p[1], succProb[i]])
            if p[1] not in hmp:
                hmp[p[1]] = []  # [node, prob]
            hmp[p[1]].append([p[0], succProb[i]])

        prob = [-float('inf')] * n
        prob[start] = 1
        heap = [(1, start)]

        while heap:  # greedy BFS, get max from each layer, until meet the end
            currProb, currNode = heapq.heappop(
                heap)  # currProb is a negative number in the heap, for it to be popped first, using abs below to calc
            if currNode in hmp:
                for child, nxtProb in hmp[currNode]:
                    if abs(currProb) * nxtProb > prob[child]:  # or simply use prob[currNode] to avoid using abs()
                        prob[child] = abs(currProb) * nxtProb
                        heapq.heappush(heap, (-prob[child], child))  # negate the largest, so it can be popped first

        return 0 if prob[end] == -float('inf') else prob[end]

