import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

data = [('Blog_Page_1','COURSE_1',90),('Blog_Page_1','COURSE_2',212),('Blog_Page_1','Blog_Page_2',99),('Blog_Page_6','COURSE_1',58),
        ('Blog_Page_3','COURSE_4',401),('Blog_Page_3','COURSE_2',2),('Blog_Page_6','Blog_Page_2',309),('Blog_Page_1','COURSE_3',306),
        ('Blog_Page_3','Blog_Page_2',41),('Blog_Page_11','COURSE_1',122),('Blog_Page_2','Blog_Page_6',39),('Blog_Page_2','COURSE_4',224),
        ('Blog_Page_11','COURSE_3',201),('Blog_Page_11','COURSE_4',89),('Blog_Page_6','Blog_Page_3',309),('Blog_Page_1','Blog_Page_3',76)
        ]

df = pd.DataFrame(data=data, columns=['node1', 'node2', 'edge'])

G = nx.DiGraph()
G.add_weighted_edges_from(data)
pos = nx.spring_layout(G, k=1000)
nx.draw(G, pos, with_labels=True)
# plt.show()

#2 часть
'''
Нужно ответить на вопрос, является ли рассматриваемый граф сильно связным или слабо связным, помогут соответствующие методы библиотеки NetworkX: is_strongly_connected(G) и is_weakly_connected(G), которые возвращают значения True или False. 
В качестве параметра G следует указать имя графа. 
Также рассчитаем количество сильно и слабо связных компонентов в графе с помощью методов nx.number_strongly_connected_components(G) и nx.number_ weakly _connected_components(G). 
Выведем самый большой сильный и самый большой слабый связные компоненты исходного графа.
Определите в рассматриваемом графе пользовательского движения по веб-сайту, кратчайший путь с отдельной страницы блога на конкретную страницу курса. 
Определите общее количество этих переходов за сутки (сумма кликов) из этого взвешенного пути, используя алгоритм Дейкстры
'''
# print('Исходный граф является сильно связным?:', nx.is_strongly_connected(G))
# print('Сильно связные компоненты: ', max(nx.strongly_connected_components(G),  key=len))
# print('Число сильно связных компонентов в исходном графе:', nx.number_strongly_connected_components(G))
# print('-----------------------------------------')
# print('Исходный граф является слабо связным?:', nx.is_weakly_connected(G))
# print('Слабо связные компоненты: ', max(nx.weakly_connected_components(G), key=len))
# print('Число слабо связных компонентов в исходном графе:', nx.number_weakly_connected_components(G))

length, path = nx.single_source_dijkstra(G, source='Blog_Page_1', target='COURSE_4')
print('Вес пути(число кликов) из страницы Blog_Page_1 на страницу  COURSE_4 = ',length)
print('Пусть из страницы Blog_Page_1 на страницу COURSE_4:', path)




