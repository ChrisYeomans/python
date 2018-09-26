import sys, math

lst = sys.stdin.readline().split()
num1 = int(lst[0])
num2 = int(lst[1])

def numFlip(n):
	flpd = 0
	modTemp = n%10
	flpd += modTemp*100
	n = math.floor(n/10)
	modTemp = n%10
	flpd += modTemp*10
	n = math.floor(n/10)
	modTemp = n%10
	flpd += modTemp*1
	return(flpd)

print(max(numFlip(num1), numFlip(num2)))