class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = address.split('.')
        r = ""
        for s in l:
            r = r + s
            r = r + "[.]"
        return r[:-3]