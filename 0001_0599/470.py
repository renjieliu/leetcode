# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
# RL: 1-10 , probability should be 1/10.
# P(a) = 0.5
# P(b) = 0.2
# P(a)*P(b) = 0.1
class Solution:
    def rand10(self):
        a = 7
        b = 7
        while a == 7:
            a = rand7()

        while b > 5:
            b = rand7()

        if a < 4:
            a = 5
        else:
            a = 0
        return a + b