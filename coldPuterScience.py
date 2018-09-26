import sys

in1 = sys.stdin.readline()
inMain = sys.stdin.readline().split()
ticker = 0
for i in inMain:
	if int(i) < 0:
		ticker+=1
	else:
		pass
print(ticker)