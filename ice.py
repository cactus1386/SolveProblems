# https://quera.org/problemset/3429
def ice():
    degree = int(input())
    if degree < 0:
        print('Ice')
    elif degree > 100:
        print('Steam')

    else:
        print('Water')


ice()
