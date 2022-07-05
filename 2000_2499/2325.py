class Solution:
    def decodeMessage(self, key: str, message: str) -> str: #O( N | N )
        hmp = {}
        for c in key:
            if c != " " and c not in hmp: 
                hmp[c] = chr(97+len(hmp))  #map the current letter to the corresponding English letter.
                
        output = ""
        for c in message:
            output += " " if c == " " else hmp[c]
        return output
    

