
def countWay(n):
	if n<0:
		return 0
	if n==0:
		return 1
	if n==1:
		result = 1
	elif n>0:
		result = countWay(n-1) + countWay(n-2) + countWay(n-3)
	return result


print(countWay(10))


def Method2(n):
	memo = [-1] * (n+1)
	return Triple(n,memo)

def Triple(n,memo):
	if n<0:
		return 0
	memo[0] = 1
	if n>=1:
		memo[1] = 1
	if n>=2:
		memo[2] = memo[1] + memo[0]
	if n>2:
		for i in range(3,n+1):
			memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
	return memo[n]


print(Method2(10))