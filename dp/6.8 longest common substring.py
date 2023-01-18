def lcs(x, y):
	n = len(x)
	m = len(y)
	opt = [[0 for _ in range(m+1)] for _ in range(n+1)]
	res = 0
	
	for i in range(1, n+1):
		for j in range(1, m+1):
			if x[i-1] == y[j-1]:
				opt[i][j] = 1 + opt[i-1][j-1]
				res = max(opt[i][j], res)
			else:
				opt[i][j] = 0
	return res

print(5, lcs("GeeksforGeeks", "GeeksQuiz"))
print(4, lcs("abcdxyz", "xyzabcd"))
print(6, lcs("zxabcdezy", "yzabcdezx"))
print(0, lcs("abc", "efg"))