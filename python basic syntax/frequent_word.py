"""
Given the text: the first line contains the number of lines, then given the lines of words.
Print the word in the text that occurs most often. If there are many such words,
print the one that is less in the alphabetical order.
"""


words = {}
for _ in range(int(input())):
    words_list = [i for i in input().split()]
    for elem in words_list:
        words[elem] = words.get(elem, 0) + 1

print(min(key for key, value in sorted(words.items()) if value == max(words.values())))
