n = int(input())
for k in range(1, n+1):
  a = 0
  b = 0
  c = 0
  d = 0
  e = 0
  num = int(input())
  while num != 1:
    if num % 2 == 0:
      a += 1
      num /= 2
    elif num % 3 == 0:
      b += 1
      num /= 3
    elif num % 5 == 0:
      c += 1
      num /= 5
    elif num % 7 == 0:
      d += 1
      num /= 7
    elif num % 11 == 0:
      e += 1
      num /= 11
  print(f'#{k}',a,b,c,d,e)
