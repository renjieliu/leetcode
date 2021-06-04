class Solution:
    def openLock(self, deadends: 'List[str]', target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        elif target == "0000":
            return 0
        else:
            def change(s):
                output = []
                for i, c in enumerate(s):
                    if int(c) == 0:
                        fill_1 = 9
                        fill_2 = 1
                    else:
                        fill_1 = (int(c)-1)%10
                        fill_2 = (int(c)+1)%10
                    output.append(s[:i] + str(fill_1)+ s[i+1:])
                    output.append(s[:i] + str(fill_2)+ s[i+1:])
                return output
            stk = [target]
            seen = set(target)
            cnt = 0
            while stk: #BFS from the target to 0000 and avoid the deadend
                nxt = []
                cnt += 1
                while stk:
                    curr = stk.pop()
                    for turn in change(curr):
                        if turn == "0000":
                            return cnt
                        else:
                            if turn not in deadends and turn not in seen:
                                nxt.append(turn)
                                seen.add(turn)
                stk=nxt

            return -1











