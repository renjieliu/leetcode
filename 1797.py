class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.tokenPool = {}
        self.ttl = timeToLive


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenPool[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenPool and self.tokenPool[tokenId] + self.ttl <= currentTime:
            del self.tokenPool[tokenId]
        if tokenId in self.tokenPool:
            self.tokenPool[tokenId] = currentTime


    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for k, v in self.tokenPool.items():
            cnt += 1 if v + self.ttl > currentTime else 0
        return cnt




    # Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

