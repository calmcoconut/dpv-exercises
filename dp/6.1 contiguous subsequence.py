"""
A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S. For
instance, if S is
	5, 15, −30, 10, −5, 40, 10,

then 15, −30, 10 is a contiguous subsequence but 5, 15, 40 is not. Give a linear-time algorithm for
the following task:
  Input: A list of numbers, a1, a2, . . . , an.
  Output: The contiguous subsequence of maximum sum (a subsequence of length zero
has sum zero).

For the preceding example, the answer would be 10, −5, 40, 10, with a sum of 55.
(Hint: For each j ∈ {1, 2, . . . , n}, consider contiguous subsequences ending exactly at position j.)
"""

def contiguousSub(lst):
	n = len(lst)
	optimal = [0] * n # base case index 0 = 0
	for i in range(1,n):
		optimal[i] = max(0,optimal[i-1] + lst[i])
	return optimal[n-1]

example = [5, 15, -30, 10, -5, 40, 10]
print("given %s, the optimal contiguous sum is %d" % (example, contiguousSub(example)))
