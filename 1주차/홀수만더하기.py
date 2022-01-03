n = int(input())
for k in range(1, n+1):
  num = list(map(int, input().split()))
  summ = 0
  for i in range(len(num)):
    if num[i] % 2 != 0:
      summ += num[i]
  print(f'#{k}',summ)
