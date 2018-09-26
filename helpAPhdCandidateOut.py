import sys

num = sys.stdin.readline()

for i in sys.stdin:
	if len(i.split("+")) == 2:
		nLst = i.split("+")
		n1 = int(nLst[0])
		n2 = int(nLst[1])
		print(n1+n2)
	else:
		print("skipped")