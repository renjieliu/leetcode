class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('G','G').replace('(al)','al').replace('()', 'o')