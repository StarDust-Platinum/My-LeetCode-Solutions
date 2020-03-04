class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def func(x):
            return x[0]**2+x[1]**2
        
        return sorted(points, key=func)[:K]