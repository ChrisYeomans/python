import sys

for i in sys.stdin:
	inpLst = i.split(" ")
	num1 = int(inpLst[0])
	num2 = int(inpLst[1])
	if num1 == 0 & num2 == 0:
		break;

	num1Steps = 0
	num2Steps = 0
	meetNum = 0
	num1Tmp = num1
	num2Tmp = num2
	num1Lst = []
	num2Lst = []

	while num1Tmp > 1:
		num1Lst.append(num1Tmp)
		if num1Tmp%2==0:
			num1Tmp = num1Tmp/2
		elif num1Tmp%2==1:
			num1Tmp = num1Tmp*3+1

	while num2Tmp > 1:
		num2Lst.append(num2Tmp)
		if num2Tmp%2==0:
			num2Tmp = num2Tmp/2
		elif num2Tmp%2==1:
			num2Tmp = num2Tmp*3+1

	for i in num2Lst:
		if i in num1Lst:
			meetNum = i
			num1Steps = num1Lst.index(i)
			num2Steps = num2Lst.index(i)
			break;

	print(num1,"needs",num1Steps,"steps,",num2,"needs",num2Steps,"steps, they meet at",meetNum)