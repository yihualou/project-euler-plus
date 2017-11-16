t = int(input())
for i in range(t):
  n = int(input())
  a, b = 1, 2
  s = 0
  while b < n:
    s += b
    at, bt = a, b
    a = 2 * bt + at
    b = 3 * bt + 2 * at
  print(s)
  