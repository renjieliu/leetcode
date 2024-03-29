class Solution:
    def calPoints(self, ops: 'List[str]') -> int: #O(N | N)
        stk = []
        total = 0
        for c in ops: # go through the arr and check one by one
            if c == "C":
                total -= stk.pop()
            else:
                if c == "D":
                    stk.append(stk[-1]*2)
                elif c == "+":
                    stk.append(stk[-1] + stk[-2])
                else:
                    stk.append(int(c))
                total += stk[-1]
        return total



# previous solution


# def calPoints(ops):
#     """
#     :type ops: List[str]
#     :rtype: int
#     """
#     temp = list(ops)
#     i = 0
#     while i<len(temp):
#         if temp[i] == "C":
#             temp.remove(temp[i])
#             temp.remove(temp[i-1])
#             i -= 2

#         elif temp[i] == "D":
#             temp[i] = int(temp[i-1])*2

#         elif  temp[i] == "+":
#             temp[i]= int(temp[i-1]) + int(temp[i-2] if i-2 >= 0 else 0)
#         i += 1

#     sum = 0
#     for i in temp:
#         sum += int(i)

#     return sum

# print(calPoints(["15483","-20523","C","C","9061","26083","+","C","4702","+","D","10260","-525","C","+","15023","-20005","-1647","C","-12853","20706","D","-21983","24892","10570","D","1215","D","D","+","3854","20505","C","D","-18850","-2170","27914","-26175","+","3188","+","+","21804","D","+","-847","D","26184","14945","C","D","+","+","13795","+","1839","15755","2627","-2090","C","C","29743","24319","D","-22624","20374","+","D","2631","+","7296","-5109","9454","-10466","D","C","+","17555","+","12144","D","16710","27969","22863","D","8521","+","D","C","-25486","-1137","9782","25633","-12031","-11248","+","C","-13559","D","D"]))
# print(calPoints(["-60","D","-36","30","13","C","C","-33","53","79"]))





