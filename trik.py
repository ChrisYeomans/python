import sys

strtLst = [1, 0, 0]

def A(lst):
	tmpLst = lst[:]
	lst[0] = tmpLst[1]
	lst[1] = tmpLst[0]
	return(lst)

def B(lst):
	tmpLst = lst[:]
	lst[1] = tmpLst[2]
	lst[2] = tmpLst[1]
	return(lst)

def C(lst):
	tmpLst = lst[:]
	lst[0] = tmpLst[2]
	lst[2] = tmpLst[0]
	return(lst)

inpStr = sys.stdin.readline()
for i in inpStr:
	if i == 'A':
		strtLst = A(strtLst)
	elif i == 'B':
		strtLst = B(strtLst)
	elif i == 'C':
		strtLst = C(strtLst)

print(strtLst.index(1)+1)