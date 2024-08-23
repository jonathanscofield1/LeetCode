class Solution:

    def get_diagonal(self,matrix, y, x):
        while y >= 0 and x >= 0:
            try:
                yield matrix[y][x]
                y -= 1
                x -= 1
            except:
                y -= 1
                x -= 1


    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        width = len(matrix[0])
        heigth = len(matrix)
        return_bool = True
        
        for i in range(0, heigth):
            diagonals = [set(self.get_diagonal(matrix, i, j)) for j in range(0, width)]
            for k in diagonals:
                if len(k) != 1:
                    return_bool = False
        return return_bool

        
       
         


        