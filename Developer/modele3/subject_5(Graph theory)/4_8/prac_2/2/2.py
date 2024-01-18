'''
Внести исходные данные в массив построить на его основе датафрейм, который будет использоваться для дальнейшего анализа.
Визуализировать исходные данные, построить марковскую цепь пользовательского поведения как направленный граф с помощью библиотеки Networkx
Сгруппировать данные по каналам привлечения
Построить гистрограмму
'''
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#Пример реализации DataFrame
# df = pd.DataFrame({
#     'country': ['Russia', 'Spain', 'Portugal', 'Romania'],
#     'population': [12.4, 543.3, 21.6, 25.9]
# })
# print(df)
# print(df['country'])


data = [('TG','COURSE_1',0.5),('RSA','COURSE_2',0.3),('Blog','COURSE_2',0.7),('Blog','COURSE_1',0.4),
('Blog','COURSE_4',0.4),('TG','COURSE_2',0.2),('Email','Blog',0.3),('RSA','COURSE_3',0.2),
('Blog','Blog_Page_2',0.1),('YouTube','COURSE_1',0.2),('Email',' COURSE_6',0.3),('TG','COURSE_4',0.2),
('RSA','COURSE_3',0.2),('Blog','COURSE_4',0.9),('Blog',' COURSE_6',0.9),('Email',' COURSE _3',0.3)
]

df = pd.DataFrame(data=data, columns=['Channel', 'Page', 'Weight'])
#Настройка и отображение графа
G = nx.DiGraph()
G.add_weighted_edges_from(data)
pos = nx.spring_layout(G, k=1000)
nx.draw(G, pos, with_labels=True)
plt.show()

#Сгруппировать данные по каналам привлечения
group = df.groupby(['Channel']).sum(sum(df['Weight']))
print(group)

#Построить гистрограмму
x = [i for i in range(len(group))]
plt.title('Результаты по привлечению клиентов')
plt.bar(x, group['Weight'])
plt.plot(group)
plt.show()






