import sys

while True:
	inpStr = sys.stdin.readline()
	inpStr = inpStr.rstrip()
	inpNum = int(inpStr)
	if inpNum == 0:
		break
	n = 11

	def sumNum(strNum):
		total = 0
		for i in strNum:
			total += int(i)
		return(total)

	while True:
		if sumNum(inpStr) == sumNum(str(inpNum*n)):
			print(n)
			break
		else:
			n += 1