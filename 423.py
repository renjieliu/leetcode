class Solution:
    def originalDigits(self, s: str) -> str:
        output = [""] * 10
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1

        if 'z' in hmp:  # for 0
            cnt = hmp['z']
            output[0] = '0' * cnt
            del hmp['z']
            hmp['e'] -= cnt
            hmp['r'] -= cnt
            hmp['o'] -= cnt
            if hmp['e'] == 0: del hmp['e']
            if hmp['r'] == 0: del hmp['r']
            if hmp['o'] == 0: del hmp['o']

        if 'g' in hmp:  # for 8
            cnt = hmp['g']
            output[8] = '8' * cnt
            del hmp['g']
            hmp['e'] -= cnt
            hmp['i'] -= cnt
            hmp['h'] -= cnt
            hmp['t'] -= cnt
            if hmp['e'] == 0: del hmp['e']
            if hmp['i'] == 0: del hmp['i']
            if hmp['h'] == 0: del hmp['h']
            if hmp['t'] == 0: del hmp['t']

        if 'x' in hmp:  # for 6
            cnt = hmp['x']
            output[6] = '6' * cnt
            del hmp['x']
            hmp['s'] -= cnt
            hmp['i'] -= cnt
            if hmp['s'] == 0: del hmp['s']
            if hmp['i'] == 0: del hmp['i']

        if 'w' in hmp:  # for 2
            cnt = hmp['w']
            output[2] = '2' * cnt
            del hmp['w']
            hmp['t'] -= cnt
            hmp['o'] -= cnt
            if hmp['t'] == 0: del hmp['t']
            if hmp['o'] == 0: del hmp['o']

        if 'u' in hmp:  # for 4
            cnt = hmp['u']
            output[4] = '4' * cnt
            del hmp['u']
            hmp['f'] -= cnt
            hmp['o'] -= cnt
            hmp['r'] -= cnt
            if hmp['f'] == 0: del hmp['f']
            if hmp['o'] == 0: del hmp['o']
            if hmp['r'] == 0: del hmp['r']

        if 's' in hmp:  # for 7
            cnt = hmp['s']
            output[7] = '7' * cnt
            del hmp['s']
            hmp['e'] -= cnt * 2
            hmp['v'] -= cnt
            hmp['n'] -= cnt
            if hmp['n'] == 0: del hmp['n']
            if hmp['v'] == 0: del hmp['v']
            if hmp['e'] == 0: del hmp['e']

        if 'o' in hmp:  # for 1
            cnt = hmp['o']
            output[1] = '1' * cnt
            del hmp['o']
            hmp['n'] -= cnt
            hmp['e'] -= cnt
            if hmp['n'] == 0: del hmp['n']
            if hmp['e'] == 0: del hmp['e']

        if 'v' in hmp:  # for 5
            cnt = hmp['v']
            output[5] = '5' * cnt
            del hmp['v']
            hmp['f'] -= cnt
            hmp['i'] -= cnt
            hmp['e'] -= cnt
            if hmp['f'] == 0: del hmp['f']
            if hmp['i'] == 0: del hmp['i']
            if hmp['e'] == 0: del hmp['e']

        if 'r' in hmp:  # for 3
            cnt = hmp['r']
            output[3] = '3' * cnt
            del hmp['r']
            hmp['t'] -= cnt
            hmp['h'] -= cnt
            hmp['e'] -= cnt * 2

            if hmp['t'] == 0: del hmp['t']
            if hmp['h'] == 0: del hmp['h']
            if hmp['e'] == 0: del hmp['e']

        if 'n' in hmp:  # for 9
            cnt = hmp['n'] // 2
            output[9] = '9' * cnt
            del hmp['n']
            hmp['i'] -= cnt
            hmp['e'] -= cnt
            if hmp['i'] == 0: del hmp['i']
            if hmp['e'] == 0: del hmp['e']

        return "".join(output)



















