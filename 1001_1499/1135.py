class Solution:
    def minimumCost(self, n: int, connections: 'List[List[int]]') -> int:
        def union(root_of_city, size_of_tree, a, b):
            root_a = find(root_of_city, a)
            root_b = find(root_of_city, b)
            if root_a == root_b:  #they are on the same tree already
                return -1
            else:
                if size_of_tree[root_a] >= size_of_tree[root_b]: #merge the smaller tree to the bigger one
                    root_of_city[root_b] = root_a
                    size_of_tree[root_a] += size_of_tree[root_b]
                else:
                    root_of_city[root_a] = root_b
                    size_of_tree[root_b] += size_of_tree[root_a]

                return max(size_of_tree[root_a],size_of_tree[root_b] ) #return the max tree size of these 2

        def find(root, a): #not really O(1), as zero or one recursion is required.
            if root[a] == a: #along side the path to the root, point each node to the root.
                return a
            root[a] = find(root, root[a])
            return root[a]

        root_of_city = [i for i in range(n+1)] #record the root of the city
        size_of_tree = [1 for r in root_of_city] #initially, each city is on it's own

        connections.sort(key = lambda x: x[2]) # Kruskal's algorithm
        output = 0
        while connections:
            c1, c2, cost = connections.pop(0)
            res = union(root_of_city, size_of_tree, c1, c2) #eventually, every city will be merged to the same tree
            if res != -1:
                output += cost
                if res == n : # every city has been connected
                    return output
        return -1


