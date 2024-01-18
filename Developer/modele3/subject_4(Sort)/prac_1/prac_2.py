from collections import defaultdict

document_text = open('test.txt', 'r')
text_string = document_text.read().lower()
words = defaultdict(int)
for line in text_string.splitlines():
    for word in line.strip().split():
        words[word] += 1

frequency = defaultdict(list)
for word, freq in words.items():
    frequency[freq].append(word)

for freq, words in sorted(frequency.items(), key=lambda x: x[0], reverse=True):
    for word in sorted(words):
        print(word, freq)



