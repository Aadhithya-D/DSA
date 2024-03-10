s = input()
n = ""
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in s:
  if i in alpha:
    n += i
n = n.lower()
s1 = 0
for i in n:
  s1 += ord(i) - 96
t = s1
while t > 9:
  s2 = 0
  for i in str(t):
    s2 += int(i)
  t = s2
print(t)
