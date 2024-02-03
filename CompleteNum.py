x = int(input("Enter your number: "))
r = []
result = 0

for i in range(1, x):
    if x % int(i) == 0:
        r.append(int(i))
    else:
        pass

for n in r:
    result += n

if int(result) == x:
    print("YES")
else:
    print("NO")
