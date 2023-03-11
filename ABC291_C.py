import io
import sys

_INPUT = """\
6
5
RLURU
20
URDDLLUUURRRDDDDLLLL
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  S=input()
  ans='No'
  now=(0,0)
  used=set()
  used.add(now)
  for i in range(N):
    nx,ny=now
    if S[i]=='R': nx+=1
    elif S[i]=='L': nx-=1
    elif S[i]=='U': ny+=1
    else: ny-=1
    now=(nx,ny)
    if now in used: ans='Yes'
    else: used.add(now)
  print(ans)