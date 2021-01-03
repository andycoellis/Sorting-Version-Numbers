from code.solution import solution, tokenizer, convert_to_list, label_list, Version

import pytest

@pytest.mark.parametrize('l, r, result', [
	(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
		["0.1","1.1.1","1.2","1.2.1","1.11","2","2.0","2.0.0"], True),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
		["1.0","1.0.2","1.0.12","1.1.2","1.3.3"], True),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "0.0.1", "1", "1.0.0"],
		["0.0.1","1","1.0","1.0.0","1.0.2","1.0.12","1.1.2","1.3.3"], True),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "0.0.1", "1", "1.0.0"],
		["0.0.1","1","1.0","1.0.0","1.0.2","1.0.12","1.1.2","1.3"], False)
	])
def test_solution(l, result):
	""" Checks that the solution is ouputed in correct order """
	assert (solution(l) == r) == result


def test_list_min_size_constraints():
	""" Tests that list > 0 """

	l = []
	with pytest.raises(ValueError):
		solution(l)


def test_list_max_size_constraints():
	""" Tests that list <=100 """

	l = []
	for i in range(0, 101):
		l.append(i.__str__())

	with pytest.raises(ValueError):
		solution(l)


@pytest.mark.parametrize('l', [
	(["1,11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]),
	(["1.11", "2.0.0", "1.A", "2", "0.1", "1.2.1", "1.1.1", "2.0"]),
	(["1.11", "2.0.0", "%"]),
	(["1.11", "2.0.0", ".1.2"]),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1..2", "0.0.1", "1", "1.0.0"]),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.2..", "0.0.1", "1", "1.0.0"]),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "0.0.1.1", "1", "1.0.0"]),
	(["01.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]),
	(["1.1.2", "1.00", "1.3.3", "1.0.12", "1.0.2"]),
	(["1.1.2", "1.0", "1.3.03", "1.0.12", "1.0.2"])
	])
def test_language(l):
	""" Check that language acceptor rejects wrong characters """
	with pytest.raises(ValueError):
		solution(l)


@pytest.mark.parametrize('l, result', [
	(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
		[[1, 11],[2, 0, 0],[1, 2],[2],[0, 1],[1, 2, 1], [1, 1, 1], [2, 0]])
	])
def test_split(l, result):
	""" Check that string is tokenized correctly """
	assert tokenizer(l) == result


@pytest.mark.parametrize('a, b, result', [
	(Version([0,1,1234]), Version([0,0,1234]), False),
	(Version([0,1,1]), Version([0,1,11]), True),
	(Version([0,1,1]), Version([0,1,1]), False),
	(Version([1,1,1]), Version([0,1,1]), False),
	(Version([1,0,0]), Version([0,20,10]), False),
	(Version([0]), Version([0,0,0]), True),
	(Version([0,1,0]), Version([0,1]), False)
	])
def test_version_class_lt(a, b, result):
	assert (a < b) == result


@pytest.mark.parametrize('a, b, result', [
	(Version([0,1,1234]), Version([0,0,1234]), True),
	(Version([0,1,1]), Version([0,1,11]), False),
	(Version([0,1,1]), Version([0,1,1]), False),
	(Version([1,1,1]), Version([0,1,1]), True),
	(Version([1,0,0]), Version([0,20,10]), True),
	(Version([0,0,0]), Version([0]), True),
	(Version([0,1,0]), Version([0,1]), True)
	])
def test_version_class_gt(a, b, result):
	assert (a > b) == result


@pytest.mark.parametrize('a, b, result', [
	(Version([0,1,1234]), Version([0,0,1234]), False),
	(Version([0,1,1]), Version([0,1,11]), False),
	(Version([0,1,1]), Version([0,1,1]), True),
	(Version([1,1,1]), Version([0,1,1]), False),
	(Version([999,87,812]), Version([999,87,812]), True),
	(Version([0,0,0]), Version([0]), False),
	(Version([0,1,0]), Version([0,1]), False)
	])
def test_version_class_eq(a, b, result):
	assert (a == b) == result


@pytest.mark.parametrize('a, result', [
	(Version([0,1,1223]), "0.1.1223"),
	(Version([12,22,2123]), "12.22.2123"),
	(Version([1,0]), "1.0"),
	(Version([0]), "0"),
	(Version([0,0,2]), "0.0.2")
	])
def test_version_class_str(a, result):
	assert a.__str__() == result


@pytest.mark.parametrize('a, result', [
	(Version([1, 0]), [1,0,0]), 
	(Version([1]), [1,0,0]),
	(Version([1,0,0]), [1,0,0]),
	(Version([0]), [0,0,0])
	])
def test_convert_to_list(a, result):
	assert convert_to_list(a) == result


@pytest.mark.parametrize('a, b, result', [
	(Version([1,0]), Version([1,1,1]), ['E','L','L']),
	(Version([0,23,4]), Version([1]), ['L','G','G']),
	(Version([123,123,123]), Version([0]), ['G','G','G']),
	(Version([1]), Version([1,0,0]), ['E','E','E']),
	(Version([0,0,1]), Version([0]), ['E','E','G'])
	])
def test_label_list(a, b, result):
	
	a = convert_to_list(a)
	b = convert_to_list(b)
	check = label_list(a, b)

	assert check == result


