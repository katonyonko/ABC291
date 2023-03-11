import io
import sys

_INPUT = """\
6
3
0 1 3
0 2 3
5
1 6 1 4 3
0 6 4 0 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import numpy as np
  def Convolve(f, g):
    fft_len = 1
    while 2 * fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    fft_len *= 2
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)
    Fh = Ff * Fg
    h = np.fft.irfft(Fh, fft_len)
    h = np.rint(h).astype(np.int64)
    return h[:len(f) + len(g) - 1]
  N=int(input())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  ans=[]
  for i in range(6):
    x=[1-((A[j]>>i)&1) for j in range(N)]
    y=[1-((B[j]>>i)&1) for j in range(N)]
    tmp=Convolve(x,y[::-1])
    tmp2=[]
    for i in range(N-1):
      tmp2.append(N-tmp[i]-tmp[i+N])
    tmp2.append(N-tmp[N-1])
    ans.append(tmp2)
  ans2=0
  for i in range(N):
    ans2=max(ans2,sum([ans[j][i]*(1<<j) for j in range(6)]))
  print(ans2)