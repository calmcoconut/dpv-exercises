def pal(st):
	n = len(st)
	opt = [[0 for _ in range(n)] for _ in range(n)]
	for i in range(n):
		opt[i][i] = 1
	
	for s in range(2, n+1):
		for i in range(n-s+1):
			j = i + s - 1
			if st[i] == st[j]:
				opt[i][j] = 2 + opt[i+1][j-1]
			else:
				opt[i][j] = max(opt[i+1][j], opt[i][j-1])
	return opt[0][n-1]

print("hello", pal("hello"))
print("sad", pal("sad"))
print("happa", pal("happa"))
print("acgtgtcaaaatcg", pal("acgtgtcaaaatcg"))