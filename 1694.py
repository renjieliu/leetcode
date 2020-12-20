class Solution:
    def reformatNumber(self, number: str) -> str:
        output = [""]
        number = number.replace(".", "").replace("-", "").replace(" ", "")
        if len(number) in (2, 3):
            return number
        elif len(number) == 4:
            return number[:2] + "-" + number[2:]
        else:
            number = list(number)
            if len(number) % 3 == 0:
                for n in number:
                    if len(output[-1]) < 3:
                        output[-1] += n
                    else:
                        output.append(n)
            elif len(number) % 3 == 1:
                for n in number[:-4]:
                    if len(output[-1]) < 3:
                        output[-1] += n
                    else:
                        output.append(n)
                for n in number[-4:]:
                    if len(output[-1]) < 2:
                        output[-1] += n
                    else:
                        output.append(n)

            elif len(number) % 3 == 2:
                for n in number[:-2]:
                    if len(output[-1]) < 3:
                        output[-1] += n
                    else:
                        output.append(n)
                for n in number[-2:]:
                    if len(output[-1]) < 2:
                        output[-1] += n
                    else:
                        output.append(n)
            return "-".join(output)






