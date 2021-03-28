class Solution:
    def originalDigits(self, s: str) -> str:
        def clean(keys, hmp):
            for k in keys:
                if hmp[k] == 0:
                    del hmp[k]

        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1
        arr = [0 for _ in range(10)]
        if "z" in hmp:
            arr[0] = hmp["z"]
            hmp["e"] -= hmp["z"]
            hmp["r"] -= hmp["z"]
            hmp["o"] -= hmp["z"]
            hmp["z"] = 0
            clean(list(hmp.keys()), hmp)
        # print(hmp)
        if "x" in hmp:
            arr[6] = hmp["x"]
            hmp["s"] -= hmp["x"]
            hmp["i"] -= hmp["x"]
            hmp["x"] = 0
            clean(list(hmp.keys()), hmp)
        if "g" in hmp:
            arr[8] = hmp["g"]
            hmp["e"] -= hmp["g"]
            hmp["i"] -= hmp["g"]
            hmp["h"] -= hmp["g"]
            hmp["t"] -= hmp["g"]
            hmp["g"] = 0
            clean(list(hmp.keys()), hmp)
        if "w" in hmp:
            arr[2] = hmp["w"]
            hmp["t"] -= hmp["w"]
            hmp["o"] -= hmp["w"]
            hmp["w"] = 0
            clean(list(hmp.keys()), hmp)
        if "s" in hmp:
            arr[7] = hmp["s"]
            hmp["e"] -= hmp["s"] * 2
            hmp["v"] -= hmp["s"]
            hmp["n"] -= hmp["s"]
            hmp["s"] = 0
            clean(list(hmp.keys()), hmp)
        # print(hmp)
        if "v" in hmp:
            arr[5] = hmp["v"]
            hmp["f"] -= hmp["v"]
            hmp["i"] -= hmp["v"]
            hmp["e"] -= hmp["v"]
            hmp["v"] = 0
            clean(list(hmp.keys()), hmp)
        # print(hmp)
        if "i" in hmp:
            arr[9] = hmp["i"]
            hmp["n"] -= hmp["i"] * 2
            hmp["e"] -= hmp["i"]
            hmp["i"] = 0
            clean(list(hmp.keys()), hmp)
        if "u" in hmp:
            arr[4] = hmp["u"]
            hmp["f"] -= hmp["u"]
            hmp["o"] -= hmp["u"]
            hmp["r"] -= hmp["u"]
            hmp["u"] = 0
            clean(list(hmp.keys()), hmp)
        if "n" in hmp:
            arr[1] = hmp["n"]
            hmp["o"] -= hmp["n"]
            hmp["e"] -= hmp["n"]
            hmp["n"] = 0
            clean(list(hmp.keys()), hmp)
        if "h" in hmp:
            arr[3] = hmp["h"]

        output = ""
        for i, a in enumerate(arr):
            output += str(i) * a
        return output















