import sys

mainLst = [
	'A', 'B', 'C', 'D', 'E', 'F', 'G',
	'H', 'I', 'J', 'K', 'L', 'M', 'N',
	'O', 'P', 'Q', 'R', 'S', 'T', 'U',
	'V', 'W', 'X', 'Y', 'Z', '_', '.'
]

for i in sys.stdin:
	rotNum = int(i.split()[0])
	if rotNum == 0:
		break
	plnTxt = i.split()[1]
	t = -1
	rotTxt = ""
	for j in range(len(plnTxt)):
		rotTxt = rotTxt + plnTxt[t]
		t-=1
	encdLst = []
	for i in rotTxt:
		ind = mainLst.index(i)
		encdLst.append(mainLst[(ind+rotNum)%28])
	print(''.join(encdLst))