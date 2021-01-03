def solution(l):
	# List length checks
	if len(l) < 1 or len(l) > 100:
		raise ValueError("The number of elements in the list must be at least 1 and not exceed 100")

	# Language acceptor checks, regular expression
	import re
	pattern = re.compile("^([0]|[1-9]|[1-9][0-9]+)(\.([0]|[1-9]|[1-9][0-9]+)){0,2}$")

	for item in l:
		if not pattern.match(item):
			raise ValueError("An item does not fill the language format")

	# Convert list of strings into a list of ints
	l = tokenizer(l)

	# Sorted list of version numbers
	mergeSort(l)

	# Convert list into output string
	convert_list_to_strings(l)

	return l


def mergeSort(l):
	""" 
	Implemented version of foundational sorting algorithm merge sort,
	algorithm based off 'geeks for geeks' website=https://www.geeksforgeeks.org/merge-sort/

	"""
	if len(l) > 1:
		mid_point = len(l)//2
		
		left_half = l[:mid_point]
		right_half = l[mid_point:]

		mergeSort(left_half)
		mergeSort(right_half)

		i = j = k = 0

		while i < len(left_half) and j < len(right_half):
			if Version(left_half[i]) < Version(right_half[j]):
				l[k] = left_half[i]
				i += 1
			else:
				l[k] = right_half[j]
				j += 1
			k += 1

		while i < len(left_half):
			l[k] = left_half[i]
			i += 1
			k += 1

		while j < len(right_half):
			l[k] = right_half[j]
			j += 1
			k += 1


def convert_list_to_strings(l):
	""" Converts a given list into the desired string representation"""
	for i in range(0, len(l)):
		l[i] = str(Version(l[i]))


def tokenizer(l):
	"""
	Returns an ordered array of integers converterd from serialised strings
	"""
	solution = []
	for word in l:
		number = word.split('.')
		
		for i in range(0, len(number)):
			number[i] = int(number[i])

		solution.append(number)

	return solution


def convert_to_list(l):
	""" Returns a blanket three digit version number of given argument """
	version_list = [0] * 3

	for i in range(0, len(l)):
		version_list[i] = l[i]

	return version_list


def label_list(v, o):
	"""
	Returns a list of labels that signify the relationship between two lists:
	
	E: Equals
	L: Less Than
	G: Greate Than
	"""
	check = [None] * 3
	for i in range(0, len(v)):

		if v[i] == o[i]:
			check[i] = 'E'
		elif v[i] < o[i]:
			check[i] = 'L'
		else:
			check[i] = 'G'

	return check


class Version(list):
	"""
	This is a representation of a version number, this allows for 
	operator overriding functionality that allows cleaner code
	"""
	def __init__(self, v):
		self.v = []
		self.length = len(v)

		for item in v:
			self.v.append(item)


	def __eq__(self, o):
		check = self.check_equivalence(o)

		return True if check == 'E'  else False

	
	def __lt__(self, o):
		check = self.check_equivalence(o)

		return True if check == 'L' else False
		

	def __gt__(self, o):
		check = self.check_equivalence(o)

		return True if check == 'G' else False


	def __str__(self):
		response = None

		for i in range(0, len(self.v)):
			if i == 0:
				response = str(self.v[i])
			else:
				response = response + '.' + str(self.v[i])

		return response


	def __len__(self):
		return len(self.v)


	def __getitem__(self, i):
		return self.v[i]

	def check_equivalence(self, o):
		""" Returns the appropriate label {'E', 'L', 'G'} of conditional property """
		check = label_list(convert_to_list(self.v), convert_to_list(o))

		count = 0
		for item in check:
			if item == 'E':
				count += 1
		# Version numbers must be exactly equal in length and number to pass		
		response = 'E' if count == 3 else None

		if response is None:
			for item in check:
				if response is None and item != 'E':
					response = item

		if response == 'E' and (len(self.v) != len(o)):
			if len(self.v) < len(o):
				response = 'L'
			else:
				response = 'G'

		return response