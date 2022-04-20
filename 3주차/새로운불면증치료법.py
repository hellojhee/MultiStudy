T = int(input())

for i in range(1, T+1):
  N = int(input())
  nlist = [0]*10
  cnt = 1
  while 0 in nlist:
    num = str(cnt * N)
    for j in range(len(num)):
      nlist[int(num[j])] += 1
    cnt += 1
  print(f'#{i} {num}')