class Solution:
    def timeRequiredToBuy(self, tickets: 'List[int]', k: int) -> int:
        cnt = 0 
        i = 0 
        while True:#simulation for the k customer to purchase the ticket
            if tickets[i] > 0:
                cnt +=1 
                tickets[i]-=1 
            if tickets[k] == 0:
                return cnt
            i = (i+1)%len(tickets)

