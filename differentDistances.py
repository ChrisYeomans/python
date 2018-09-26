import sys

def metricDist(x1, y1, x2, y2, p):
	return(((abs(x1-x2))**p + abs((y1-y2))**p)**(1/p))

for i in sys.stdin:
	lneLst = i.split()
	if float(lneLst[0]) == 0:
		break
	X1 = float(lneLst[0])
	Y1 = float(lneLst[1])
	X2 = float(lneLst[2])
	Y2 = float(lneLst[3])
	P = float(lneLst[4])
	print(metricDist(X1, Y1, X2, Y2, P))