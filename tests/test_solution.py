from code.solution import solution, tokenizer, version

import pytest

@pytest.mark.parametrize('l, result', [
	(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
		"0.1,1.1.1,1.2,1.2.1,1.11,2,2.0,2.0.0"),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
		"1.0,1.0.2,1.0.12,1.1.2,1.3.3"),
	(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2", "0.0.1", "1", "1.0.0"],
		"0.0.1,1,1.0,1.0.0,1.0.2,1.0.12,1.1.2,1.3.3")
	])
def test_solution(l, result):
	""" Checks that the solution is ouputed in correct order """
	assert solution(l) == result


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
	(version([0,1,1234]), version([0,0,1234]), False),
	(version([0,1,1]), version([0,1,11]), True),
	(version([0,1,1]), version([0,1,1]), False),
	(version([1,1,1]), version([0,1,1]), False),
	(version([1,0,0]), version([0,20,10]), False)
	])
def test_version_class_lt(a, b, result):
	assert a < b == result


@pytest.mark.parametrize('a, b, result', [
	(version([0,1,1234]), version([0,0,1234]), True),
	(version([0,1,1]), version([0,1,11]), False),
	(version([0,1,1]), version([0,1,1]), False),
	(version([1,1,1]), version([0,1,1]), True),
	(version([1,0,0]), version([0,20,10]), True)
	])
def test_version_class_gt(a, b, result):
	assert a > b == result


@pytest.mark.parametrize('a, b, result', [
	(version([0,1,1234]), version([0,0,1234]), False),
	(version([0,1,1]), version([0,1,11]), False),
	(version([0,1,1]), version([0,1,1]), True),
	(version([1,1,1]), version([0,1,1]), False),
	(version([999,87,812]), version([999,87,812]), True)
	])
def test_version_class_eq(a, b, result):
	assert (a == b) == result


@pytest.mark.parametrize('a, result', [
	(version([0,1,1223]), "0, 1, 1223"),
	(version([12,22,2123]), "12, 22, 2123")
	])
def test_version_class_str(a, result):
	assert a.__str__() == result

