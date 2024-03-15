# https://quera.org/problemset/221462
def third_place():
    a = []
    b = []
    c = []
    result = []
    for i in range(0, 7):
        inp = input('')
        stringList = inp.split()
        a.append(int(stringList[0]))
        b.append(int(stringList[1]))
        c.append(int(stringList[2]))
    num = a[0]
    count = a.count(num)
    if count == 3:
        result.append(num)
    else:
        for i in range(0, 4):
            a.remove(num)
        result.append(a[0])

    num = b[0]
    count = b.count(num)
    if count == 3:
        result.append(num)
    else:
        for i in range(0, 4):
            b.remove(num)
        result.append(b[0])

    num = c[0]
    count = c.count(num)
    if count == 3:
        result.append(num)
    else:
        for i in range(0, 4):
            c.remove(num)
        result.append(c[0])

    print(f'{result[0]} {result[1]} {result[2]}')


third_place()
