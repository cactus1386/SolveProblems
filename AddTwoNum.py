l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]

a = ''
for i in range(len(l1)):
    a = a + str(l1[i])
    a_num = int(a)

b = ''
for i in range(len(l2)):
    b = b + str(l2[i])
    b_num = int(b)

c_num = a_num + b_num
print(c_num)