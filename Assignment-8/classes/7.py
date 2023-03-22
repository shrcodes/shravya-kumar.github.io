#Write a Python class to reverse a string word by word.Input string : 'hello.py' Expected Output : '.py hello’
class StringReverser:
    def reverse_words(self, s: str) -> str:
        words = s.split()
        reversed_words = words[::-1]
        reversed_string = ' '.join(reversed_words)
        return reversed_string