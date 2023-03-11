import io
import sys

_INPUT = """\
6
3 2
3 1
2 3
3 2
3 1
3 2
4 6
1 2
1 2
2 3
2 3
3 4
3 4
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  G=[set() for _ in range(N)]
  G2=[set() for _ in range(N)]
  for i in range(M):
    X,Y=map(lambda x: int(x)-1, input().split())
    G[Y].add(X)
    G2[X].add(Y)
  ans=[-1]*N
  node=[]
  for i in range(N):
    if len(G[i])==0: node.append(i)
  flg=0
  if len(node)>1: flg=1
  for i in range(N):
    x=node.pop()
    ans[x]=i+1
    for v in G2[x]:
      G[v].remove(x)
      if len(G[v])==0: node.append(v)
    if len(node)>1: flg=1
  if flg==0:
    print('Yes')
    print(*ans)
  else: print('No')