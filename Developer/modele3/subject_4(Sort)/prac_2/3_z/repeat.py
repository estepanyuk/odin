from collections import defaultdict

dict_word = {}
doc_text = open('text.txt', 'r')
text_str = doc_text.read().lower()

words = defaultdict(int)
for line in text_str.splitlines():
    for word in line.strip().split():
        words[word] += 1
print(words)

dict_word = defaultdict(list)
for word, i in words.items():
    dict_word[i].append(word)
print(dict_word)

for i, words in sorted(dict_word.items(), key=lambda s: s[0], reverse=True):
    for word in sorted(words):
        print(word, i)






