"""
Yuckdonald’s is considering opening a series of restaurants along Quaint Valley Highway (QVH).
The n possible locations are along a straight line, and the distances of these locations from the
start of QVH are, in miles and in increasing order, m1, m2, . . . , mn. The constraints are as follows:
• At each location, Yuckdonald’s may open at most one restaurant. The expected profit from
opening a restaurant at location i is pi, where pi > 0 and i = 1, 2, . . . , n.
• Any two restaurants should be at least k miles apart, where k is a positive integer.
Give an efficient algorithm to compute the maximum expected total profit subject to the given
constraints
"""

def yuck(m,p,k):
	n = len(m)
	opt = [0] + [p[i] for i in range(n)]

	for i in range(1,n):
		for j in range(i):
			if m[i] - m[j] >= k:
				opt[i] = max(p[i], p[i] + opt[j])
	
	print(opt)
	return opt[n-1]

stores = 		[1,2,3,4,5]
store_profit =  [10,4,8,7,11]
profit = yuck(stores,store_profit, 3)
print("yuck donalds max profit is: ", profit)

stores = 		[10,12,44,50,55]
store_profit =  [10,4,8,7,11]
profit = yuck(stores,store_profit, 3)
print("yuck donalds max profit is: ", profit)