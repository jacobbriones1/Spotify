import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import artist
from artist import Artist
from collections import OrderedDict

artist1 = Artist("Tory Lanez")
print(artist1.getEdges())
artists = np.array([])
artists = np.append(artists, artist1.artistName)
vertices=[]
edges = []
G = nx.Graph()

for i in range(artist1.nEdges):
    artists = np.append(artists, artist1.relArtistsNames[i])
    artist = Artist(artists[i])
    nodes = artist.getVertices()
    Edges= artist.getEdges()
    
    for j in range(len(nodes)):
        if (nodes[j] in G.nodes) == False:
            G.add_node(nodes[j])
            
    for j in range(len(Edges)):
        if ((Edges[j][1],Edges[j][0]) in G.edges) == False:
                G.add_edge(Edges[j][0],Edges[j][1])


colors = []
colors = colors.append('green')
Colors = [i/len(G.nodes) for i in range(len(G.nodes)) if i !=0]
colors = np.append(colors,Colors)
fig = plt.figure(figsize=(30,30))
nx.draw(G, node_color=colors,with_labels=True,font_size=19)
plt.title('Related Artists Graph',fontsize=25)
plt.show()
