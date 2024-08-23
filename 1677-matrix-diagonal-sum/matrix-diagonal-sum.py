class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        shape = len(mat)
        if shape == 1:
            return mat[0][0] 
        r_start = 0
        l_start = shape - 1
        r_diag = []
        l_diag = []

        for i in mat:
            r_diag.append(i[r_start])
            l_diag.append(i[l_start])
            r_start += 1
            l_start -= 1

        combined = [r_diag, l_diag]
        
        if shape % 2 != 0:
            remove_index = int((shape / 2) - 0.5)
            combined[0][remove_index] = 0
            print(combined)

        return sum(combined[0]) + sum(combined[1])


        


        