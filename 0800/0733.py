class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        S = set()
        h = (len(image),)
        w = (len(image[0]),)
        color = (image[sr][sc],)
        
        def search(p):
            S.add(p)
            r = p[0]
            c = p[1]
            if r-1>-1 and image[r-1][c]==color[0] and (r-1, c) not in S:
                search((r-1, c))
            if r+1<h[0] and image[r+1][c]==color[0] and (r+1, c) not in S:
                search((r+1, c))
            if c-1>-1 and image[r][c-1]==color[0] and (r, c-1) not in S:
                search((r, c-1))
            if c+1<w[0] and image[r][c+1]==color[0] and (r, c+1) not in S:
                search((r, c+1))

        search((sr, sc))
        for p in S:
            image[p[0]][p[1]] = newColor
        return image