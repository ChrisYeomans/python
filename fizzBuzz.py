import sys

inpLst = sys.stdin.readline().split()
n1 = int(inpLst[0])
n2 = int(inpLst[1])
count = int(inpLst[2])

for i in range(count):
	i+=1
	out = []
	if i%n1 == 0:
		out.append("Fizz")
	if i%n2 == 0:
		out.append("Buzz")
	if len(out) == 0:
		print(i)
	else:
		print(''.join(out))
