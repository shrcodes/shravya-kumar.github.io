#  Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
items= "red, white, black, red, green, black"
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))