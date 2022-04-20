T = int(input())

for i in range(1, T+1):
  P, Q, R, S, W = list(map(int, input().split()))
  if W <= R:
    price1 = Q
    price2 = P * W
    price = min(price1, price2)
  else:
    price1 = P * W
    price2 = Q + ((W - R) * S)
    price = min(price1, price2)
  print(f'#{i} {price}')