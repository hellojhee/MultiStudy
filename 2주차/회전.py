# 회전

T = int(input())

for i in range(1, T+1):
  N, M = map(int, input().split())
  ary = list(map(int, input().split()))

  for j in range(M):
    ary.append(ary[0])
    ary.pop(0)
  
  print(f'#{i} {ary[0]}')

