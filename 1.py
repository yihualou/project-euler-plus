def sum(v):
  return int((1 + v) * v) >> 1


t = int(input())
for i in range(t):
  n = int(input())
  l3 = int((n - 1) / 3)
  l5 = int((n - 1) / 5)
  l15 = int((n - 1) / 15)

  print(3 * sum(l3) + 5 * sum(l5) - 15 * sum(l15))

