def LargestSubmatrix(matrix):
    ans = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] != 0 and row > 0:
                matrix[row][col] += matrix[row - 1][col]

        curr = sorted(matrix[row], reverse=True) 
        for i in range(len(matrix[0])):
            ans = max(ans, curr[i] * (i + 1))
        
    return ans

A=[[0,0,1],[1,1,1],[1,0,1]]
print(LargestSubmatrix(A))
