import sys
outLst = []

for i in sys.stdin:
	a = int(i)%42
	if a in outLst:
		continue
	elif a not in outLst:
		outLst.append(a)

print(len(outLst))