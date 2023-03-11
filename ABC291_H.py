import io
import sys

_INPUT = """\
6
4
1 2
2 3
3 4
5
1 2
1 3
1 4
1 5
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from random import choice
  from collections import deque
  def bfs(G,s):
    inf=10**10
    D={s:0}
    parent={0:-1}
    D[s]=0
    used=set([s])
    dq=deque()
    dq.append(s)
    while dq:
      x=dq.popleft()
      for y in G[x]:
        if y not in D or D[y]>D[x]+1:
          D[y]=D[x]+1
          dq.append(y)
          parent[y]=x
          used.add(y)
    return D,parent,used

def cent_decomp(G,i):
  D,parent,used=bfs(G,i)
  size={key:1 for key in used}
  stack=[(i,0)]
  while stack:
    x,d=stack.pop()
    if d==0:
      for v in G[x]:
        if D[v]>D[x]:
          stack.append((v,1))
          stack.append((v,0))
    else:
      size[parent[x]]+=size[x]
  res=[]
  for i in used:
    tmp=0
    if len(used)-size[i]>len(used)//2: tmp=1
    for v in G[i]:
      if D[v]>D[i] and size[v]>len(used)//2: tmp=1
    if tmp==0: res.append(i)
  return res[0]

  from collections import defaultdict
  N=int(input())
  G=defaultdict(set)
  for i in range(N-1):
    A,B=map(lambda x: int(x)-1,input().split())
    G[A].add(B)
    G[B].add(A)
  ans=[-1]*N

  stack=[(-2,0)]
  while stack:
    y,x=stack.pop()
    c=cent_decomp(G,x)
    ans[c]=y
    vertex=G[c].copy()
    for v in vertex:
      G[c].remove(v)
      G[v].remove(c)
    for v in vertex:
      stack.append((c,v))

  print(*[ans[i]+1 for i in range(N)])