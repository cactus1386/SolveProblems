# Problem Source: https://leetcode.com/problems/longest-palindromic-substring/description
s = "babsh"

result = ""
for i in s:
    if i in result:
        result += i
        break
    else:
        result += i
print(result)
