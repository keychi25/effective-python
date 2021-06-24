def sort_priority(values: list, group: dict):
	"""sort of priority

	Args:
		values (list): 並び替えたい配列
		group (dict): 優先したい値
	"""
	def helper(x):
		if x in group:
			return (0, x)
		return (1, x)
	values.sort(key=helper)

numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)

def sort_priority2(values: list, group: dict):
	"""sort of priority

	Args:
		values (list): 並び替えたい配列
		group (dict): 優先したい値
	"""
	found = False # スコープ： 'sort_priority2'
	def helper(x):
		if x in group:
			found = True # スコープ：'helper'
			return (0, x)
		return (1, x)
	values.sort(key=helper)
	return found

found = sort_priority2(numbers, group)
print('Found', found) # 'Found', False
print(numbers)

def sort_priority3(values: list, group: dict):
	"""sort of priority

	Args:
		values (list): 並び替えたい配列
		group (dict): 優先したい値
	"""
	found = False
	def helper(x):
		nonlocal found
		if x in group:
			found = True
			return (0, x)
		return (1, x)
	values.sort(key=helper)
	return found

found = sort_priority3(numbers, group)
print('Found', found) # 'Found', True
print(numbers)

class Sorter:
	def __init__(self, group):
		self.group = group
		self.found = False
	
	def __call__(self, x):
		if x in self.group:
			self.found = True
			return (0, x)
		return (1, x)

sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True
