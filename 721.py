class Solution:
    def accountsMerge(self, accounts: 'List[List[str]]') -> 'List[List[str]]':
        root = {}
        acc = [[] for _ in range(len(accounts))]
        for i in range(len(accounts)):
            email = accounts[i][1:]
            for e in email :
                if e not in root: # the email has never been seen before
                    root[e] = i
                    acc[i].append(e)
                elif root[e] != i: # the email is seen before, attach all the people in the previous group to current
                    prev_root = root[e]
                    acc[i] += acc[prev_root]
                    for v in acc[prev_root]: # map all the email within the same group to current
                        root[v] = i
                    acc[prev_root] = [] # clear the previous

        output = []
        for i in range(len(acc)): #find the name of the person, and attach the emails
            if acc[i]:
                name = accounts[i][0]
                email = sorted(list(set(acc[i])))
                output.append( [name] + email )
        return output

