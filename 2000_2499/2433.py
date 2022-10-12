class Solution:
    def findArray(self, pref: 'List[int]') -> 'List[int]': # O( N | N )
        output = [pref[0]]
        prev = output[-1]
        
        for result in pref[1:]:
            curr = prev ^ result #prev ^ result to get current number
            output.append(curr)
            prev = result # assign current number as prev
        return output

    
