import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph() #создали объект графа

#определим список углов(ID узлов)
nodes =[1, 2, 3, 4, 5]

#определим список ребер
edges = [(1, 2), (1, 3),(2, 3), (2, 4), (3, 5),(5, 5)]

G.add_edges_from(edges)
G.add_nodes_from(nodes)

#рисуем граф и отображаем
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()



