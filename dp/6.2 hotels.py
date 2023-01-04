"""
You are going on a long trip. You start on the road at mile post 0. Along the way there are n
hotels, at mile posts a1 < a2 < · · · < an, where each ai is measured from the starting point. The
only places you are allowed to stop are at these hotels, but you can choose which of the hotels
you stop at. You must stop at the final hotel (at distance an), which is your destination.

You’d ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing
of the hotels). If you travel x miles during a day, the penalty for that day is (200 − x)^2. You want
to plan your trip so as to minimize the total penalty—that is, the sum, over all travel days, of the
daily penalties.

Give an efficient algorithm that determines the optimal sequence of hotels at which to stop
"""

def hotels(lst):
	n = len(lst)
	lst.insert(0,0)
	opt = [float("inf") for _ in range(n+1)]
	opt[0] = 0
	stops = [0 for _ in range(n+1)]
	path = []
	
	for cur in range(1,n+1):
		for prev in range(cur):
			p = opt[prev] + (200-(lst[cur]-lst[prev]))**2
			if p < opt[cur]:
				opt[cur] = p
				stops[cur] = prev
	k=n
	print(stops)
	while k > 0:
		path.insert(0, stops[k])
		k = stops[k]
		
	print(opt)
	return opt[n], path

def hotels2(lst):
	n = len(lst)
	opt = [float("inf")] * (n+1)
	opt[0] = 0
	lst.insert(0,0)

	for i in range(1,n+1):
		for j in range(i):
			diff = (200-(lst[i] - lst[j]))**2 + opt[j]
			opt[i] = min(opt[i], diff)
	return opt[n] , []

example = [100,300,400,500, 900]
res, path = hotels2(example)
print("for hotels %s the lowest penalty is %d by stopping at hotels %s" % (example, res,path))
