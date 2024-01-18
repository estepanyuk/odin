import matplotlib.pyplot as plt
import networkx as nx

#создать объект графа
G = nx.Graph()

nodes = [1, 2, 3, 4, 5]
edges = [(1, 2), (1,3), (2,3), (2,4), (3,5), (5,5)]

#добавляем информацию в наш объект
G.add_nodes_from(nodes)
G.add_edges_from(edges)

#рисуем граф и отображаем его
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
