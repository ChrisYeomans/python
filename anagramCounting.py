import sys, math

def uniqCntr(inpStr):
	tmpDct = {}
	for i in inpStr:
		if i in tmpDct:
			tmpDct[i]+=1
		else:
			tmpDct[i] = 1
	cntr = 1
	for j in tmpDct:
		if j != 0:
			cntr = cntr*(1/tmpDct[j])
	#print(cntr)
	return(cntr)

for l in sys.stdin:
	l = l.strip()
	#print(len(l))
	x = float(math.factorial(len(l))*uniqCntr(l))
	print(int(x))