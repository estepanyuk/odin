from pyvis.network import Network

#создаем объект графа
net = Network(notebook=True)

#добавление узлов
net.add_nodes(
    #id узла
    [1, 2, 3, 4, 5],
    label=['Node #1','Node #2','Node #3','Node #4','Node #5'],
    #будет отображаться при наведении мыши
    title=['Main node', 'Just node','Just node', 'Just node', 'Node with self-loop'],
    color=['#369c89','#deb41b','#de311b','#1bb0de','#de1bca']
)

#определим список ребер
net.add_edges([(1, 2), (1, 3), (2, 3), (2, 4), (3, 5), (5, 5)])

net.show('graph.html')
