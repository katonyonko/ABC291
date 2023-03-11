import io
import sys

_INPUT = """\
6
3
1 2
4 2
3 4
4
1 5
2 6
3 7
4 8
8
877914575 602436426
861648772 623690081
476190629 262703497
971407775 628894325
822804784 450968417
161735902 822804784
161735902 822804784
822804784 161735902
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  mod=998244353 
  N=int(input())
  cards=[list(map(int,input().split())) for _ in range(N)]
  dp=[0]*(2*N)
  dp[0]=1
  dp[1]=1
  for i in range(N-1):
    if cards[i][0]!=cards[i+1][0]: dp[(i+1)*2]=(dp[(i+1)*2]+dp[i*2])%mod
    if cards[i][0]!=cards[i+1][1]: dp[(i+1)*2+1]=(dp[(i+1)*2+1]+dp[i*2])%mod
    if cards[i][1]!=cards[i+1][0]: dp[(i+1)*2]=(dp[(i+1)*2]+dp[i*2+1])%mod
    if cards[i][1]!=cards[i+1][1]: dp[(i+1)*2+1]=(dp[(i+1)*2+1]+dp[i*2+1])%mod
  print(sum(dp[-2:])%mod)