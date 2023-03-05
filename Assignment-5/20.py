# Write a Python program to remove all consecutive duplicates of a given string.
str=input('')
seen = str[0]
ans = str[0]
for i in str[1:]:
    if i != seen:
        ans += i
        seen = i
print(ans)
