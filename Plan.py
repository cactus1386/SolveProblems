# https://quera.org/problemset/221462
def third_place():
    a = []
    result = []
    for i in range(0, 7):
        inp = input('')
        stringList = inp.split()
        a.append(int(stringList[0]))
    num = a[0]
    count = a.count(num)
    if count == 3:
        result.append(num)
    else:
        for i in range(0, 4):
            a.remove(num)
        result.append(a[0])

    print(result)


third_place()
