class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.r = len(self.history) - 1 #the right pointer

    def visit(self, url: str) -> None:
        self.history = self.history[:self.r + 1] + [url]
        self.r = len(self.history) - 1

    def back(self, steps: int) -> str:
        if steps >= self.r + 1:  # len(self.history):
            output = self.history[0]
            self.r = 0
        else:
            self.r -= steps
            output = self.history[self.r]
        return output

    def forward(self, steps: int) -> str:
        if steps >= len(self.history) - 1 - self.r:
            output = self.history[-1]
            self.r = len(self.history) - 1
        else:
            self.r += steps
            output = self.history[self.r]

        return output

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)