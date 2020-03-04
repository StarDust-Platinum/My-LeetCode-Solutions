class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = dict()
        ans = []
        for i in range(len(numbers)):
            if numbers[i] not in d.keys():
                d[numbers[i]] = [i+1, 1]
            else:
                d[numbers[i]][1] += 1
        for x in numbers:
            if target-x in numbers:
                if target-x!=x:
                    return [d[x][0], d[target-x][0]]
                    return ans
                elif d[x][1]>1:
                    return [d[x][0], d[x][0]+1]