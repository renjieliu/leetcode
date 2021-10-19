class FreqStack:

    def __init__(self):
        self.currMost = 0  # highest frequency
        self.freq = {}  # number in each freq
        self.cnt = {}  # track how many times the number has been pushed

    def push(self, x: int) -> None:
        if x not in self.cnt:
            self.cnt[x] = 0
        self.cnt[x] += 1
        c = self.cnt[x]
        if c not in self.freq:
            self.freq[c] = []
        self.freq[c].append(x)
        self.currMost = max(c, self.currMost)

    def pop(self) -> int:
        curr = self.currMost
        output = self.freq[curr].pop()
        if self.freq[curr] == []:
            del self.freq[curr]
            self.currMost -= 1

        self.cnt[output] -= 1
        if self.cnt[output] == 0:
            del self.cnt[output]

        return output

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()


# previous approach
# class FreqStack:
#
#     def __init__(self):
#         self.stk = []  # main stack
#         self.num_freq = {}
#         self.freq_pos = {}  # count of each stacked number
#         self.max_freq = -float('inf')
#
#     def push(self, x: int) -> None:
#         self.stk.append(x)
#         if x not in self.num_freq:
#             self.num_freq[x] = 0
#         self.num_freq[x] += 1
#         t = self.num_freq[x]  # frequence of current number
#         if t not in self.freq_pos:
#             self.freq_pos[t] = []
#         self.freq_pos[t].append(len(self.stk) - 1)
#
#         self.max_freq = max(self.max_freq, t)  # current max freq
#
#     def pop(self) -> int:
#         f = self.max_freq
#         pos = self.freq_pos[f].pop()  # find the frequency pos, from the rightmost to left
#         if self.freq_pos[f] == []:  # current cnt has been exausted
#             del self.freq_pos[f]
#             self.max_freq -= 1
#         suspect = self.stk[pos]
#         self.stk[pos] = 'removed'  # not physically removed, as the index of other elements will change
#         self.num_freq[suspect] -= 1
#         if self.num_freq[suspect] == 0:
#             del self.num_freq[suspect]
#
#         return suspect
#
# # Your FreqStack object will be instantiated and called as such:
# # obj = FreqStack()
# # obj.push(x)
# # param_2 = obj.pop()