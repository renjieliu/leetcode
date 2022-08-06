class Solution(object):
    def mirrorReflection(self, p, q): # RL 20220804 copied solution, O( N | 1 )
        from fractions import Fraction as F

        x = y = 0
        rx, ry = p, q
        targets = [(p, 0), (p, p), (0, p)]

        while (x, y) not in targets:
            #Want smallest t so that some x + rx, y + ry is 0 or p
            #x + rxt = 0, then t = -x/rx etc.
            t = float('inf')
            for v in [F(-x,rx), F(-y,ry), F(p-x,rx), F(p-y,ry)]:
                if v > 0: t = min(t, v)

            x += rx * t
            y += ry * t

            #update rx, ry
            if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
                rx *= -1
            if y == p or y == 0:
                ry *= -1

        return 1 if x==y==p else 0 if x==p else 2
    
    



# previous solution 

# class Solution(object):
#     def mirrorReflection(self, p, q):
#         from fractions import Fraction as F

#         x = y = 0
#         rx, ry = p, q
#         targets = [(p, 0), (p, p), (0, p)]

#         while (x, y) not in targets:
#             #Want smallest t so that some x + rx, y + ry is 0 or p
#             #x + rxt = 0, then t = -x/rx etc.
#             t = float('inf')
#             for v in [F(-x,rx), F(-y,ry), F(p-x,rx), F(p-y,ry)]:
#                 if v > 0: t = min(t, v)

#             x += rx * t
#             y += ry * t

#             #update rx, ry
#             if x == p or x == 0: # bounced from east/west wall, so reflect on y axis
#                 rx *= -1
#             if y == p or y == 0:
#                 ry *= -1

#         return 1 if x==y==p else 0 if x==p else 2







