# 숫자 추가

T = int(input())

for i in range(1, T+1):
  N, M, L = map(int, input().split())
  ary = list(map(int, input().split()))

  for j in range(1, M+1):
    index, num =  map(int, input().split())
    ary.append(None)

    for k in range(len(ary)-1, index, -1):
      ary[k] = ary[k-1]
      ary[k-1] = None
    ary[index] = num

  print(f'#{i} {ary[L]}')

