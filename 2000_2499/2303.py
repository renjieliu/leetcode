class Solution:
    def calculateTax(self, brackets: 'List[List[int]]', income: int) -> float: #O( N | 1 )
        if income <= brackets[0][0]:
            return brackets[0][1] * income/100
        else:
            output = brackets[0][0] * brackets[0][1] /100
            for i in range(1, len(brackets)):
                if income > brackets[i][0]: #pay full tax for the current bracket
                    output += brackets[i][1] * (brackets[i][0] - brackets[i-1][0]) / 100
                else:
                    output += max(0, income - brackets[i-1][0]) * brackets[i][1] / 100 #delta with previous bracket, pay current tax
            return output
                    

