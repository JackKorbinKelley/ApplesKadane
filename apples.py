# Coding Challenge
# Given an array of integers representing the number of apples on each tree
# Determine the maximum number of apples two people can pick without crossing paths
# Each person can pick n apples


# Solution adapted from Kadane's Algorithm
# O(n) runtime
# O(1) storage

def apples(n,trees):
	if not len(trees) >= 2*n:
		return ("Error: not enough trees.")
	index = 0
  	l_max = 0
  	t_max = 0
  	left, right = None, None

  	while index <= len(trees)-(2*n):
	  	l_max = max(l_max, sum(trees[index:index+n]))
	  	t_max = max(t_max, l_max + sum(trees[index+n:index+(2*n)]))
	  	index += 1

	return t_max

# Test Examples
print(apples(5, [1,0,9,1,0,1,2,3,11,0,11,0,1,2,31,0,1,2,3,1,0,1,2,3,19,21,0,1,2,3,2,3,0,1,2,32,3,1,0,1,1,0,1,2,32,30,19,1,0,1,2,31,0,1,2,3]))
print(apples(5, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,9,1,1,1,1,1,22]))
print(apples(1, [1,0,9,1,0,1,2,3,11,0,11,0,1,2,31,0,1,2,3,1,0,1,2,3,19,21,0,1,2,3,2,3,0,1,2,32,3,1,0,1,1,0,1,2,32,30,19,1,0,1,2,31,0,1,2,3]))
print(apples(10, [1,0,9,1,0,1,2,3,11,0,11,0,1,2,31,0,1,2,3,1,0,1,2,3,19,21,0,1,2,3,2,3,0,1,2,32,3,1,0,1,1,0,1,2,32,30,19,1,0,1,2,31,0,1,2,3]))