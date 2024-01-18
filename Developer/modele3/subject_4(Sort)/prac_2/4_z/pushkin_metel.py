import string

import nltk
from nltk import word_tokenize

from nltk.probability import FreqDist

#загрузка данных
f = open('pushkin-metel.txt', 'r', encoding='utf-8')
text = f.read()

#предварительная обработка текста
text = text.lower()
spec_punct = string.punctuation + '\n\xa0''\t-...'

#для удаления не нужных символов
def remove_punct_from_text(text, punct):
    return ''.join([pun for pun in text if pun not in punct])

text = remove_punct_from_text(text, spec_punct)
text = remove_punct_from_text(text, string.digits)

#токенизация
text_tokens = word_tokenize(text)
text = nltk.Text(text_tokens)

#Подсчет слов
fdist = FreqDist(text)

#график
fdist.plot(30, cumulative=False)





