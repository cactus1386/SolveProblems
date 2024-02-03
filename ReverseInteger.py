x = 320
r = ''

for i in reversed(str(x)):
    if i == '-':
        negetive = True
        pass
    else:
        negetive = False
        r += i

if negetive:
    result = int(('-' + r))
    print(result)

else:
    result = int(r)
    print(result)