class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        triangles = list(itertools.combinations(points, 3))
        max_area = 0
        for t in triangles:
            A, B, C = t[0], t[1], t[2]
            area = abs(A[0]*(B[1]-C[1])+B[0]*(C[1]-A[1])+C[0]*(A[1]-B[1]))/2
            if area > max_area:
                max_area = area
        return max_area