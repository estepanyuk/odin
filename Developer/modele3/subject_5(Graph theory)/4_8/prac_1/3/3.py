import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

data = [('Blog_Page_1','COURSE_1',90),('Blog_Page_1','COURSE_2',212),('Blog_Page_1','Blog_Page_2',99),('Blog_Page_6','COURSE_1',58),
        ('Blog_Page_3','COURSE_4',401),('Blog_Page_3','COURSE_2',2),('Blog_Page_6','Blog_Page_2',309),('Blog_Page_1','COURSE_3',306),
        ('Blog_Page_3','Blog_Page_2',41),('Blog_Page_11','COURSE_1',122),('Blog_Page_2','Blog_Page_6',39),('Blog_Page_2','COURSE_4',224),
        ('Blog_Page_11','COURSE_3',201),('Blog_Page_11','COURSE_4',89),('Blog_Page_6','Blog_Page_3',309),('Blog_Page_1','Blog_Page_3',76)
        ]

df = pd.DataFrame(data=data, columns=['node1','node2','edge'])
graph = nx.DiGraph()
graph.add_weighted_edges_from(data)
pos = nx.spring_layout(graph, k=1000)
nx.draw(graph, pos, with_labels=True)
plt.show()

