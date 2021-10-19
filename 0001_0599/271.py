class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        output = ""
        for s in strs:
            output += str(len(
                s)) + " " + s  # how many characters to take (prefix and space), to form string like  "0 3 abc1 12 1_"
        return output

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        output = []
        i = 0
        num = ""
        while i < len(s):  # each time read the prefix (how many characters to take)
            while s[i] != " ":
                num += s[i]
                i += 1
            if int(num) == 0:
                output.append("")
            else:
                output.append(s[i + 1: i + 1 + int(num)])
            i += int(num) + 1  # advance i to the end of the taken string
            num = ""
        return output

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))