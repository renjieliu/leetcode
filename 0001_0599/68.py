class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: int) -> 'List[str]':
        def adjust(s, width):  # s, how many words are there, width
            arr = s.split(" ")
            if len(arr) == 1:
                return arr[0] + " " * (maxWidth - len(arr[0]))
            else:
                output = ""
                space_to_add = (width - len(s)) // (len(arr) - 1)
                n = (width - len(s)) % (len(arr) - 1)  # first n need space_to_add+1 space
                i = 0
                while i < len(arr) - 1:
                    if i < n:
                        post = " " * (space_to_add + 1)
                        output += (arr[i] + " " + post)
                    else:
                        post = " " * space_to_add
                        output += (arr[i] + " " + post)
                    i += 1
                output += arr[-1]
                return output

        output = []
        curr = ""
        i = 0
        while i < len(words):
            to_be = curr + (" " if curr != "" else "") + words[i]
            if len(to_be) < maxWidth:
                curr = to_be
                i += 1
            elif len(to_be) == maxWidth:
                output.append(to_be)
                curr = ""
                i += 1
            elif len(to_be) > maxWidth:  # need to adjust current
                output.append(adjust(curr, maxWidth))
                curr = ""

        if curr != "":
            post = " " * (maxWidth - len(curr))
            output.append(curr + post)
        return output

