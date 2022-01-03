n = int(input())
for k in range(1, n+1):
  num = input()
  date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  month = int(num[4:6])
  day = int(num[6:8])
  if month >12 or month == 0:
    print(f'#{k}', '-1')
  elif day == 0 or day > date[month-1]:
    print(f'#{k}', '-1')
  else:
    print(f'#{k}', f'{num[:4]}/{num[4:6]}/{num[6:]}')
