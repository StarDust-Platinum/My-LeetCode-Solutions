class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        if ds.keys()!=dt.keys():
            return False
        for key in ds.keys():
            if ds[key]!=dt[key]:
                return False
        return True