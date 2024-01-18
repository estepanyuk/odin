import matplotlib.pyplot as plt
import networkx as nx

G = nx.cubical_graph()
pos = nx.spring_layout(G, send=313794652) #позиция всех узлов

#узлы
option = {'engecolor': 'tab:gray', 'node_size': 800, 'alpha': 0.9}
nx.draw_networkx_nodes(G, )
nx.draw_networkx_nodes()