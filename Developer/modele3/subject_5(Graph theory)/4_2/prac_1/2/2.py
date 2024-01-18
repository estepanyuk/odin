from pyvis.network import Network

#создать объект графа
G = Network(notebook=True)

#добавление узлов

G.add_nodes(
    [1, 2, 3, 4, 5],
    label=['Node#1','Node#2','Node#3','Node#4','Node#5'],
    title=['Main node','Just node','Just node','Just node','Node with self-loop'],
    color=['#DC143C','#20B2AA','#FFFF00','#8B008B','#006400']
)

G.add_edges([(1, 2), (1,3), (2,3), (2,4), (3,5), (5,5)])

G.show('graph.html')