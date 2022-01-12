# 반복 문자 지우기

T = int(input())

for i in range(1, T+1):
  txt = input()
  stack = []
  stack.append(txt[0])

  for j in range(1, len(txt)):

    if len(stack) == 0:
      stack.append(txt[j])

    elif txt[j] == stack[-1]:
      stack.pop()
      
    else:
      stack.append(txt[j])

  if len(stack) == 0:
    print(f'#{i}', 0)
  else:
    print(f'#{i} {len(stack)}')

