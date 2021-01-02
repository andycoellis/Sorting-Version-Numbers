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