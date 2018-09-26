import math, sys

for i in sys.stdin:
	a = i.split(" ")
	b = int(a[0])
	c = int(a[1])
	print(abs(b-c))