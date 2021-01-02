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

	return l


def tokenizer(w):

	return w
