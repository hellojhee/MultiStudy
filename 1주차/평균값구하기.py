n = int(input())
for k in range(1, n+1):
  num = list(map(int, input().split()))
  summ = 0
  for i in range(len(num)):
    summ += num[i]
    meann = summ / len(num)
  print(f'#{k}', f'{meann:.0f}')
