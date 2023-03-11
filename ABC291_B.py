import io
import sys

_INPUT = """\
6
1
10 100 20 50 30
2
3 3 3 4 5 6 7 8 99 100
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  X=sorted(list(map(int,input().split())))
  print(sum(X[N:4*N])/(3*N))