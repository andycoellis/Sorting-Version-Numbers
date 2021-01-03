# Sorting-Version-Numbers
Algorithm to sort version numbers presented as string, given as a coding challenge

* **Author:** [Andrew Ellis](https://www.linkedin.com/in/andrew-ellis-3a199113b/)

*Please be aware that more specific information about the challenge has been hidden as to keep company name and challenge secret*

### Overview
The challenge required to take in a list of strings as such, ```["1.1.2", "4", "2.3", "0.0.123"]``` and return a sorted list in ascending order: 
```0.0.123, 1.1.2, 4, 2.3```. Another requirement listed was that "The number of elements in the list l will be at least 1 and will not exceed 100."

There were three main parts to this challenge when approaching:
1. Validate all incoming lists for edge cases that may break requirements or version number expectations
2. Tokenize all strings into seperate lists that allow for integer conditional properties
3. Sort items using [merge sort](https://www.geeksforgeeks.org/merge-sort/) that would allow for space and time complexity of O(n log (n))

Additionally, I wanted to utilse this experience with building upwards with [Test Driven Development](https://www.martinfowler.com/bliki/TestDrivenDevelopment.html). This also meant that I would be able to utilise [GitHub Actions](https://github.com/features/actions), furthering my knowledge and skills in [Continuous Integration](https://www.atlassian.com/continuous-delivery/continuous-integration).

### Specifications
* Python 2.7.13

### Packages
* [PyTest 5.0.1](https://docs.pytest.org/en/latest/)

### Notes on project

* I found that in order to best implement a clean version of the merge sort algorithm I would have to create an class object of each string of *version numbers* this allowed me to overload operators as found below.

```python
	def __eq__(self, o):
	
	def __lt__(self, o):

	def __gt__(self, o):

	def __str__(self):

	def __len__(self):

	def __getitem__(self, i):
```

* This made such blocks of code much more readable for observors, this can be seen where the class ```Version``` is implemented

```python
		while i < len(left_half) and j < len(right_half):
			if Version(left_half[i]) < Version(right_half[j]):
				l[k] = left_half[i]
				i += 1
			else:
				l[k] = right_half[j]
				j += 1
			k += 1
```

Other noteworthy aspects I found in the challenge was the use of ```pytest``` as the testing framework, this allowed for ease integration with *GitHub Actions* and also was convenient for adding multiple parameters in the test cases. *An example can be found below...*

```python
@pytest.mark.parametrize('a, result', [
	(Version([1, 0]), [1,0,0]), 
	(Version([1]), [1,0,0]),
	(Version([1,0,0]), [1,0,0]),
	(Version([0]), [0,0,0])
	])
def test_convert_to_list(a, result):
	assert convert_to_list(a) == result
```
