class Solution:
	def matrixScore(self, grid: List[List[int]]) -> int:
		row, col = len(grid), len(grid[0])
		for x in range(row):
			if grid[x][0] == 0:
				for y in range(col):
					if grid[x][y] == 1:
						grid[x][y] = 0

					else:
						grid[x][y] = 1

		for y in range(col):
			onesCount = 0
			for x in range(row):
				if grid[x][y] == 1:
					onesCount += 1

			if onesCount < row - onesCount: # less ones than zeros
				for x in range(row):
					if grid[x][y] == 1:
						grid[x][y] = 0

					else: 
						grid[x][y] = 1

		result = 0
		for i in range(row):
			for j in range(col):
				if grid[i][j] == 1:
					result += 2**(col-j-1)

		return result