class Solution:
    def findSubstring(s: str, words: 'List[str]'):
        if words == []:
            return []

        elif s == "":
            return [] if "" not in words else [words.index("")]

        elif len(s) < len(words) * len(words[0]):  # total lenth of the list
            return []

        else:
            word_dict = {}
            for w in words:  # build the lookup dict
                if w not in word_dict:
                    word_dict[w] = 0
                word_dict[w] += 1

            output = []
            i = 0
            width = len(words[0])
            len_all = len(words) * width

            while i < len(s) - len_all + 1:  # no need to check if it's shorter than the combined
                curr = s[i:i + len_all]
                j = 0
                shadow = word_dict.copy()

                while j < len(curr) - width + 1:  # check within the current window
                    x = curr[j:j + width]
                    # print(curr, x, shadow)
                    if x in shadow:
                        shadow[x] -= 1
                        if shadow[x] == 0:
                            del shadow[x]
                        if shadow == {}:  # all the words are found, and the curr should also be exhausted
                            output.append(i)
                            break
                    else:
                        break  # as long as it cannot be found in the current string, it should go back to the outer loop

                    j += width

                i += 1

            return output

