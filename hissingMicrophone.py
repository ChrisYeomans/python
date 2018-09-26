import sys

strung = sys.stdin.readline()
strung = strung.lower()
out = "no hiss"
hissTick = False

for i in strung:
	if i == 's':
		if hissTick == True:
			out = "hiss"
			break
		elif hissTick != True:
			hissTick = True
	else:
		hissTick = False

print(out)