class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Initialize the triangle with the first row
        triangle = []

        for i in range(numRows):
            # Start each row with 1s; a row has (i + 1) elements
            row = [1] * (i + 1)
            
            # Fill in the middle elements (from index 1 to i-1)
            for j in range(1, i):
                # The element is the sum of the two above it in the previous row
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            
            triangle.append(row)
            
        return triangle