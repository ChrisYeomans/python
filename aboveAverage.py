import sys, decimal


def avg(lst):
	totSum = 0
	for i in range(len(lst)):
		totSum+=float(lst[i])
	return(totSum/len(lst))

def prcpAbove(lst):
	cnt = 0
	avrg = avg(lst)
	for i in lst:
		if float(i) > avrg:
			cnt+=1
	return(round((cnt/len(lst))*100, 3))

in1 = sys.stdin.readline()
for i in sys.stdin:
	inpLst = i.split()
	del inpLst[0]
	ans = decimal.Decimal(prcpAbove(inpLst))
	ans = str(decimal.Decimal(ans.quantize(decimal.Decimal('.001'), rounding=decimal.ROUND_HALF_UP)))
	ans+="%"
	print(ans)
