class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        R,C=len(M),len(M[0])
        M2=[[0]*C for i in range(R)]
        for i in range(R):
            for j in range(C):
                temp=[M[i+x][j+y] for x,y in list(itertools.product([-1,0,1],[-1,0,1])) if 0<=i+x<R and 0<=j+y<C ]
                M2[i][j]=(sum(temp)//len(temp))
        return M2