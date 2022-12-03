from reverseSpiralReadSQMatrix import get_matrix
from createTestSQMatrix import create_square_matrix, reverse_spiral_read
import asyncio

url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
print(asyncio.run(get_matrix(url)))
matrix = create_square_matrix(5)
print(create_square_matrix(5))
print(reverse_spiral_read(matrix))