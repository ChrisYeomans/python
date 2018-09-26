import sys

shdLst = [1, 1, 2, 2, 2, 8]
inpLst = sys.stdin.readline().split()
outLst = []

for i in range(6):
	if int(inpLst[i]) != shdLst[i]:
		outLst.append(shdLst[i]-int(inpLst[i]))
	else:
		outLst.append(0)

print(' '.join(str(e) for e in outLst))