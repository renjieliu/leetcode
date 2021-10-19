class Solution:
    def makeConnected(self, n: int, connections: 'List[List[int]]') -> int:
        lkp = connections.copy()
        hmp ={}
        for x, y in lkp:
            if x not in hmp:
                hmp[x] = []
            hmp[x].append(y)
            if y not in hmp:
                hmp[y] = []
            hmp[y].append(x)
        #print(hmp)
        peer = []
        i = 0
        while hmp:
            currKey = list(hmp.keys())[0]
            peer.append([currKey])
            j = 0
            while j < len(peer[-1]):
                currFind = peer[-1][j]
                if currFind in hmp:
                    peer[-1] += hmp[currFind]
                    del hmp[currFind]
                j+=1
            i+=1
        #print(peer)
        connectedMachine = 0
        for p in peer:
            connectedMachine += len(set(p))
        toConnect = n-connectedMachine + (len(peer) - 1)# isolated machines + isolated peers
        cableNeeded = connectedMachine - 1
        over = len(connections) - cableNeeded
        return -1 if toConnect > over else toConnect