import sys, math

def diag(h ,w):
	h = int(h)
	w = int(w)
	return(math.sqrt(h**2 + w**2))

def check(n):
	n = int(n)
	if n <= diag(dimens[1], dimens[2]):
		print("DA")
	elif n > diag(dimens[1], dimens[2]):
		print("NE")

dimens = sys.stdin.readline().split(" ")
diag(dimens[1], dimens[2])

for i in sys.stdin:
	i = int(i)
	check(i)