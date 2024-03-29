class Solution:
    def accountsMerge(self, accounts: 'List[List[str]]') -> 'List[List[str]]':
        loc = {}
        groups = [[] for _ in accounts]
        for i in range(len(accounts)):
            mails = accounts[i][1:]
            for m in mails:
                if m in loc:
                    if loc[m] != i : # this mail was seen before
                        t = loc[m] # save the prev location
                        for g in groups[loc[m]]: #everyone in the same group need to be added to current
                            groups[i].append(g)
                            loc[g] = i
                        groups[t] = []
                else:
                    loc[m] = i
                    groups[i].append(m)
                
        output = []
        for i, g in enumerate(groups):
            if g: 
                output.append([accounts[i][0]]+sorted(g))
        return output
                    
           
        

# previous approach 
# class Solution:
#     def accountsMerge(self, accounts: 'List[List[str]]') -> 'List[List[str]]':
#         loc= {} # to record the location of email
#         groups = [[] for _ in accounts] 
#         for i, acc in enumerate(accounts):
#             for email in acc[1:]:
#                 if email not in loc:
#                     loc[email] = i
#                     groups[i].append(email)
#                 elif loc[email] != i: #this email was seen before 
#                     prev_loc = loc[email]
#                     for e in groups[loc[email]]: #for all the email in the same group, move to the current group
#                         loc[e] = i
#                         groups[i].append(e)
#                     groups[prev_loc] = [] #clear the previous group
        
#         output = []
#         for i, emails in enumerate(groups):
#             if emails:
#                 name = accounts[loc[emails[0]]][0]
#                 output.append([name] + sorted(emails))
#         return output
    


# previous approach
# class Solution:
#     def accountsMerge(self, accounts: 'List[List[str]]') -> 'List[List[str]]':
#         root = {}
#         acc = [[] for _ in range(len(accounts))]
#         for i in range(len(accounts)):
#             email = accounts[i][1:]
#             for e in email :
#                 if e not in root: # the email has never been seen before
#                     root[e] = i
#                     acc[i].append(e)
#                 elif root[e] != i: # the email is seen before, attach all the people in the previous group to current
#                     prev_root = root[e]
#                     acc[i] += acc[prev_root]
#                     for v in acc[prev_root]: # map all the email within the same group to current
#                         root[v] = i
#                     acc[prev_root] = [] # clear the previous

#         output = []
#         for i in range(len(acc)): #find the name of the person, and attach the emails
#             if acc[i]:
#                 name = accounts[i][0]
#                 email = sorted(list(set(acc[i])))
#                 output.append( [name] + email )
#         return output

