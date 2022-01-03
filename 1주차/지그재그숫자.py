n = int(input())
for k in range(1, n+1):
  num = int(input())
  tot = 0
  for i in range(1, num+1):
    if i % 2 != 0:
      tot += i
    elif i % 2 == 0:
      tot -= i
  print(f'#{k}', tot)
