class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        s = str(N)
        if len(s)<= 1:
            return N
        else:
            prev = s[0]
            i = 1
            output = ""
            anchor = None
            while i < len(s):
                if s[i] == s[i-1]:
                    if anchor == None:
                        anchor = i-1    #the number start at i-1 location
                elif s[i] < s[i-1]:
                    if anchor != None:
                        x = anchor
                    else:
                        x = i-1
                    output = s[:x] # anything before the anchor should be ok
                    rest = '9'*len(s[x+1:])# anything after anchor
                    change = str(int(s[x])-1) #change the anchor to the value-1
                    output += (change + rest)
                    return int(output)
                else:
                    anchor = None
                i+=1
            return N