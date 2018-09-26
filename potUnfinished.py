import sys

rnge = int(sys.stdin.readline())
tot = 0

for i in sys.stdin:
	num = i[:-2]
	pw = i[-1]
	tot += int(num.strip())**int(pw.strip())

print(tot)