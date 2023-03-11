import io
import sys

_INPUT = """\
6
aBc
xxxxxxXxxx
Zz
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  for i in range(len(S)):
    if ord('a')>ord(S[i]) or ord('z')<ord(S[i]): print(i+1)