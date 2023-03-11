import io
import sys

_INPUT = """\
6
5 2
11
01
11
10
00
6 3
101
001
101
000
100
000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  S=[input() for _ in range(N)]
  G=[[] for _ in range(N)]
  G2=[[] for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if S[i][j]=='1':
        G[i].append(i+j+1)
        G2[i+j+1].append(i)
  ds=[10**8]*N
  dg=[10**8]*N
  ds[0]=0
  dg[-1]=0
  ans=[]
  for i in range(N-1):
    for v in G[i]:
      ds[v]=min(ds[v],ds[i]+1)
    for v in G2[~i]:
      dg[v]=min(dg[v],dg[~i]+1)
  for k in range(1,N-1):
    tmp=10**8
    for f in range(max(0,k-M+1),k):
      for b in range(k+1-f,M+1):
        if S[f][b-1]=='1':
          tmp=min(tmp,ds[f]+dg[f+b]+1)
    if tmp==10**8: ans.append(-1)
    else: ans.append(tmp)
  print(*ans)