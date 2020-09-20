class Solution:
    def reorderSpaces(self, text: str) -> str:
        space_cnt = len(text) - len(text.replace(' ', ''))
        w_list = text.split(' ')
        w_cnt = sum([1 for w in w_list if w.replace(" ", "") != ""])
        if w_cnt == 1:
            for w in w_list:
                if w.replace(" ", "") != "":
                    return w + " " * space_cnt
        else:
            avg_space = space_cnt // (w_cnt - 1)
            output = ""
            for w in w_list:
                if w.replace(" ", "") != "":
                    output += (w + " " * avg_space)

            output = output.rstrip(" ")
            return output if space_cnt % (w_cnt - 1) == 0 else output + " " * (space_cnt % (w_cnt - 1))
