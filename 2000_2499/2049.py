class Solution:
    def countHighestScoreNodes(self, parents: 'List[int]') -> int:
        tree = {}
        for i, p in enumerate(parents):
            if p not in tree:
                tree[p] = []
            tree[p].append(i)
        def dfs(nodes, tree, idx):
            if idx not in tree: #node not as parent of any other node
                nodes[idx] = [1, 0, 0] #[isleaf, leftNodes, rightNodes]
                return 1 
            else:
                A = B = 0
                A = dfs(nodes, tree, tree[idx][0])
                if len(tree[idx]) == 2: 
                    B = dfs(nodes, tree, tree[idx][1])
                nodes[idx] = [0, A, B]
                return A+B+1
        
        nodes = {} #[isleaf, leftNodes, rightNodes] 
        total = len(parents)
        dfs(nodes, tree, 0) #starting from node 0 
        output = {}
        # print(tree)
        # print(total)
        # print(nodes)
        for k, v in nodes.items():
            if v[0] == 1:
                score = total-1
            else:
                score = max(1, total - 1 - v[1] -v[2] ) * max(1, v[1]) * max(1, v[2]) # left/right tree, if 0, then * 1
            if score not in output:
                output[score] = 0
            output[score] += 1
        
        return output[max(output.keys())]
        
        
        

        
        
        
