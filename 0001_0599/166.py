class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        def divide(A, B):  # [0/1, result, start_repeating_pos] 0 - non repeating 1 - repeating
            if A * B == 0:
                return [0, "0", -1]
            else:
                sign = "-" if A * B < 0 else ""
                A = abs(A)
                B = abs(B)
                p = A // B
                mod = A % B
                if mod == 0:
                    return [0, sign + str(p), -1]
                else:  # A/B, until a repeating pattern found
                    mod_arr = []
                    output = str(p) + "."
                    while mod not in mod_arr:
                        mod_arr.append(mod)
                        mod *= 10
                        output += str(mod // B)
                        mod = mod % B
                        if mod == 0:
                            return [0, sign + output, -1]
                    return [1, sign + output, mod_arr.index(mod)]  # the last part is to find where the repeating starts

        t = divide(numerator, denominator)
        if t[0] == 0:
            return t[1]
        else:
            arr = t[1].split('.')
            output = arr[0] + '.'  # integer part + .
            output += arr[1][:t[2]] + '(' + arr[1][t[2]:] + ")"  # decimal part, non repeating + ( + repeating + )
            return output

