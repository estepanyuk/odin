import string

import nltk
from nltk import word_tokenize

from nltk.probability import FreqDist

#облако
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#стоп слова
from nltk.corpus import stopwords
nltk.download('stopwords')

#для самолетика
import numpy as np
from PIL import Image

#загрузка данных
f = open('/Developer/modele3/subject_4(Sort)/prac_2/4_z/pushkin-metel.txt', 'r', encoding='utf-8')
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

stop_words = stopwords.words('russian')
stop_words.extend(['это', 'любое', 'нею'])

#самолетик
cake_mask = np.array(Image.open('plane.jpg'))

#облако, но без стоп слов
# text_raw = ' '.join(text)
# wordcloud = WordCloud().generate(text_raw)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

#облако, но со стоп словами
# text_raw = ' '.join(text)
# wordcloud = WordCloud(stopwords=stop_words).generate(text_raw)
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

#облако со стоп словами, в самолетике
text_raw = ' '.join(text)
wordcloud = WordCloud(stopwords=stop_words, mask=cake_mask, contour_width=10, contour_color='#2e3042').generate(text_raw)
plt.figure(figsize=(9,5))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()




