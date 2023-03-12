def are_anagram(s1, s2):

    if len(s1) != len(s2):
        return False

    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

s1 = "listen"
s2 = "danger"
are_anagram(s1, s2)