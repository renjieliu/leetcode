class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace('&quot;', "\"").replace("&apos;", "'").replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").replace("&frasl;", "/")