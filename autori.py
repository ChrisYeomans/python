import sys

outLst = []
nmeLst = sys.stdin.readline().split('-')
for i in nmeLst:
	outLst.append(i[0])

print(''.join(outLst))