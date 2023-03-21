from rSpiralRead import get_matrix
import createTestSQMatrix as m
import asyncio

# for x in range(0, 11):
#     try:
#         matrix = m.reverse_spiral_populate(x)
#         for row in matrix:
#             for element in row:
#                 print(str(element).rjust(len(str(x ** 2))), end=" ")
#             print()
#
#         print(f"\n{m.reverse_spiral_read(matrix)}\n")
#     except ValueError:
#         print("ERROR")

# for x in range(1, 26):
#     print(x)
#     print(float(x) % (x**0.5))

# text_data = "sdfsdfw qwe qwe ewrqkwe qwedfwe"
# matrix_data = [int(element) for element in text_data.split() if element.isdigit()]
# print(matrix_data)
# print(len(matrix_data))

url = "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
print(asyncio.run(get_matrix(url)))
