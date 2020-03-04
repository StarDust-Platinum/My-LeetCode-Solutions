class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:     
        count_dict = {}
        l = []
        for i in range(len(arr1)):
            x = arr1[i]
            if x not in arr2:
                l.append(x)
            elif x not in count_dict.keys():
                count_dict[x] = 1
            else:
                count_dict[x] += 1
        l.sort()
        res = []
        for n in arr2:
            res+=[n]*count_dict[n]
        res += l
        return res