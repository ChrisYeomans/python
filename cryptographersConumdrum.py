import sys

per = "PER"
mulPer = ""
inpStr = sys.stdin.readline()
n = int(len(inpStr)/3)
mulPer = per*n
inpStr = inpStr.upper()
ticker = 1

for i in range(len(inpStr)-1):
	if inpStr[i] == mulPer[i]:
		ticker+=1

print(len(inpStr)-ticker)