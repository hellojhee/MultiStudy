T = int(input())

for i in range(1, T+1):
  text = list(input())
  tlist = []
  for j in range(len(text)-1, -1, -1):
    tlist.append(text[j])
  for k in range(len(text)):
    if (text[k] == tlist[k]):
      ans = 1
    else:
      ans = 0
  print(f'#{i} {ans}')