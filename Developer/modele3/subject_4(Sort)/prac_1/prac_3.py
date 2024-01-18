import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Импортируем библиотеку для лемматизации русских и украинских слов
import pymorphy2
# Импортируем метод word_tokenize из библиотеки nltk
from nltk.tokenize import word_tokenize

from nltk.corpus import stopwords


stop_words = stopwords.words('russian')

# data = pd.read_csv("articles.csv")
# text = ' '.join(data['Title'])
text1 = open('test.txt', 'r')
text = text1.read().lower()

# разбиваем текст на токены
# в результате получаем переменную типа list со списком токенов
text = word_tokenize(text)

# инициализируем лемматайзер MorphAnalyzer()
lemmatizer = pymorphy2.MorphAnalyzer()


# функция для лемматизации текста, на вхд принимает список токенов
def lemmatize_text(tokens):
    # создаем переменную для хранения преобразованного текста
    text_new = ''
    # для каждого токена в тексте
    for word in tokens:
        # с помощью лемматайзера получаем основную форму
        word = lemmatizer.parse(word)
        # добавляем полученную лемму в переменную с преобразованным текстом
        text_new = text_new + ' ' + word[0].normal_form
    # возвращаем преобразованный текст
    return text_new


# вызываем функцию лемматизации для списка токенов исходного текста
text = lemmatize_text(text)

# генерируем облако слов
cloud = WordCloud(stopwords=stop_words).generate(text)
plt.imshow(cloud)
plt.axis('off')

print()