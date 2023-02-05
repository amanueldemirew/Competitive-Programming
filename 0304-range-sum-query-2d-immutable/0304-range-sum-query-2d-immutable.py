class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row, col = len(matrix), len(matrix[0])
        self.ps = [[0]*(col+1) for r in range(row+1)]
        
        for r in range(row):
            pre = 0
            for c in range(col):
                pre += matrix[r][c]
                up = self.ps[r][c+1]
                self.ps[r+1][c+1] = pre + up

        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        br = self.ps[r2+1][c2+1]
        up = self.ps[r1][c2+1]
        l = self.ps[r2+1][c1]
        tl = self.ps[r1][c1]
        return br -up - l + tl
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)