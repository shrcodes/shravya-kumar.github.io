#Write a Python function that takes a list of words and returns the length of the longest one
word_list=['Hello','Joe','Game']
max=len(word_list[0])
longest=word_list[0]
for i in word_list:
    if len(i)>max:
        max=len(i)
        longest=i
print(longest)