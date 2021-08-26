class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == "#":
            return True
        arr = preorder.split(',')
        if len(arr) < 3 or arr[-1]!='#' or arr[-2]!= '#':
            return False
        else:
            nodes = [0] if arr[0] != '#' else [] #take the first item as root

            for a in arr[1:]:
                if a != "#":
                    while nodes and nodes[-1] == 2:
                        nodes.pop()
                    if nodes:
                        nodes[-1] += 1
                    else:
                        return False
                    nodes.append(0)
                else: # current is "#"
                    if nodes:
                        if nodes[-1] < 2:
                            nodes[-1]+=1
                            while nodes and nodes[-1] == 2:
                                nodes.pop()
                        else:
                            while nodes and nodes[-1] == 2:
                                nodes.pop()
                            if nodes:
                                nodes[-1]+=1
                            else:
                                return False
                    else: # empty node list, the "#" cannot be added to any node
                        return False
                #print(a, nodes)
            return True




# previous approach
# class Solution:
#     def isValidSerialization(self, preorder: str) -> bool:
#         if len(preorder.replace(",", "")) == 2:  # the string lenth is 2, then it's not a BT
#             return False
#         elif preorder == "#":
#             return True
#         else:
#             num_stk = []
#             for i in range(len(preorder.split(","))):
#                 p = preorder.split(",")[i]
#
#                 if i > 0 and num_stk == []:  # The num_stk has been exhausted, and there's still chars left
#                     return False
#                 else:
#                     if p != "#":
#                         num_stk.append([p, 0])
#                     elif p == "#":
#                         if len(num_stk) > 0:
#                             num_stk[-1][1] += 1
#                         else:
#                             return False  # if no number exists, and it reads a # from the string, it will be invalid.
#                     if len(num_stk) > 0:
#                         while num_stk[-1][1] == 2:
#                             num_stk.pop()
#                             if num_stk == []:
#                                 break
#                             else:
#                                 num_stk[-1][1] += 1
#
#             if num_stk == []:
#                 return True
#
#             return False
#
#
#
