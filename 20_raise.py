"""
Noneを返すのではなく例外を送出する
"""

def careful_divide(a: float, b: float):
	"""[summary]

	Args:
		a (float): [description]
		b (float): [description]

	Raises:
		ValueError: When the inputs cannot be divided

	Returns:
		float: division
	"""
	try:
		return a / b
	except ZeroDivisionError:
		raise ValueError('Invaild inputs')

x, y = 5.0, 2.0
try:
	result = careful_divide(x, y)
except ValueError:
	print('Invaild inputs')
else:
	print(f'Result is {result=:0.1f}')
