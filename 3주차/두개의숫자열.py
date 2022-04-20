T = int(input())

for k in range(1, T+1):
  N, M = list(map(int, input().split())) 
  A = list(map(int, input().split()))
  B = list(map(int, input().split()))

  if N > M:
    numlist = []
    for i in range(N-M+1):
      ans = 0
      for j in range(M):
        ans += A[i+j] * B[j]
      numlist.append(ans)
      maxans = max(numlist)

  elif N < M:
    numlist = []
    for i in range(M-N+1):
      ans = 0
      for j in range(N):
        ans += A[j] * B[i+j]
      numlist.append(ans)
      maxans = max(numlist)
      
  else:
    maxans = 0
    for i in range(A):
      maxans += A[i] * B[i]

  print(f'#{k} {maxans}')