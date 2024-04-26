#pending
class Solution(object):
    def minFallingPathSum(self, grid):
        n=len(grid)
        f_m,s_m=float('inf'),float('inf')
        f_i,s_i=-1,-1
        for i in range(n):
            if i!=0:
                for j in range(n):
                    if j!=f_i: grid[i][j]+=f_m
                    else: grid[i][j]+=s_m
            f_m,s_m=float('inf'),float('inf')
            for j in range(n):
                if grid[i][j]<f_m:
                    s_m=f_m
                    f_m=grid[i][j]
                    f_i=j
                elif grid[i][j]<s_m:
                    s_m=grid[i][j]
                    s_i=j
        return min(f_m,s_m)           
