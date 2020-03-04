class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        D = {}
        D["1"],D["2"],D["3"]=None,None,None
        for i in nums:
            if D["1"]==None or i>D["1"]:
                D["3"]=D["2"]
                D["2"]=D["1"]
                D["1"]=i
            elif D["2"]==None or i>D["2"]:
                if i == D["1"]:
                    continue
                D["3"]=D["2"]
                D["2"]=i
            elif D["3"]==None or i>D["3"]:
                if i == D["2"]:
                    continue
                D["3"]=i
        if D["3"]==None:
            return D["1"]
        else:
            return D["3"]