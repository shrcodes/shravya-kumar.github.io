# Write a Python program to find smallest and largest word in a given string..
str = "This is a Sentence"
word = ""
all_words = []
str = str + " "
for i in range(0, len(str)):
	if(str[i] != ' '):
		word = word + str[i]
	else:
		all_words.append(word) 
		word = ""
 
small = large = all_words[0]
 
#Find smallest and largest word in the str  
for k in range(0, len(all_words)):
	if(len(small) > len(all_words[k])):
		small = all_words[k]
	if(len(large) < len(all_words[k])):
		large = all_words[k]
print("Smallest word: " + small)
print("Largest word: " + large)