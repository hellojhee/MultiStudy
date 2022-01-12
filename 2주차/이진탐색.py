# 이진탐색

def makeTree(n):
  global count
  if n <= N:
    makeTree(n*2)
    tree[n] = count
    count += 1
    makeTree(n*2 + 1)


T = int(input())

for i in range(1, T+1):
  N = int(input())
  tree = [0 for i in range(N+1)]
  count = 1
  makeTree(1)

  print(f'#{i} {tree[1]} {tree[N//2]}')

