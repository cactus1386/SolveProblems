s = 'babsh'

result = ''
for i in s:
    if i in result:
        result += i
        break
    else:
        result += i
print(result)