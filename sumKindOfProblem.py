import sys

num = sys.stdin.readline()

for i in sys.stdin:
	outLst = []
	inLst = i.split(" ")
	outLst.append(inLst[0])
	n = int(inLst[1])
	outLst.append(int(n*(n+1)/2))
	outLst.append(int(n*n))
	outLst.append(int(n*(n+1)))
	print(' '.join(str(e) for e in outLst))