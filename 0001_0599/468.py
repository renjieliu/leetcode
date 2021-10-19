class Solution:
    def validIPAddress(self, IP: str) -> str:
        if ":" in IP:
            stk = IP.split(':')
            valid = [str(_) for _ in range(10)] + ['a', 'b', 'c', 'd', 'e', 'f']
            if len(stk) != 8: return "Neither"
            for s in stk:
                curr = ""
                for c in s:
                    if c.lower() not in valid:
                        return "Neither"
                    curr += c
                if len(curr) > 4 or len(curr) == 0:
                    return "Neither"
            return "IPv6"


        elif "." in IP:
            stk = IP.split('.')
            if len(stk) != 4: return "Neither"
            for s in stk:
                if s.isnumeric() and len(s) == len(str(int(s))) and int(s) < 256:  # number,no leading 0,valid number
                    continue
                else:
                    return "Neither"
            return "IPv4"
        else:
            return "Neither"