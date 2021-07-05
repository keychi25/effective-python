"""mapやfilterの代わりにリスト内包表記を使う
"""

a = list(range(1, 11))
squares = []

for x in a:
	squares.append(x ** 2)
print(squares)

squares2 = [x ** 2 for x in a]
print(squares2)

alt = map(lambda x: x**2, a)
print(list(alt))

even_squares = [x **2 for x in a if x % 2 == 0]
print(even_squares)

even_alt = map(lambda x: x**2, filter(lambda x: x % 2 == 0, a))
print(list(even_alt))

even_squares_dict = {x: x ** 2 for x in a if x % 2 == 0}
print(even_squares_dict)
