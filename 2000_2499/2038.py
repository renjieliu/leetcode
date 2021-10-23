class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        #just to check how many consecutive A and B, if >= 3, then rounds = curr_count-2
        round_A = 0
        round_B = 0
        curr_a = curr_b = 0
        for c in colors:
            if c == "A":
                if curr_b >=3: 
                    round_B += (curr_b-2)
                curr_b = 0 
                curr_a += 1
            else:
                if curr_a >=3:
                    round_A += (curr_a-2)
                curr_a = 0
                curr_b += 1 
        if curr_a >= 3: 
                round_A += (curr_a-2)
        if curr_b>=3:
            round_B += (curr_b-2)
        
        # print(A, B)
        return round_A > round_B


