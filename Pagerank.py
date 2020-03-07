import networkx as nx
import os
from Url import Url
import matplotlib.pyplot as plt
 
 
with open("indexes/doc_ids.txt", "r") as ids:
    mapping = {v: k for k, v in eval(ids.readline()).items()}

def create_graph():
    graph = nx.DiGraph()
    dev_directory = "DEV/"
    graph.add_nodes_from(range(1, len(mapping)+1))
    for direct in os.listdir(dev_directory):

            if direct != '.DS_Store':
                
                for file in os.listdir(dev_directory + direct):
                    
                    # print(doc_id)
                    # posting(file) returns url and stuff for DOC_ID_DICT and for tokenizer
                    temp = Url(dev_directory + direct + '/' + file)
                    if temp.get_url() in mapping:
                        list_of_links = get_all_sublinks(temp.get_html())
                        graph.add_edges_from([(mapping[temp.get_url()], final_edge)for final_edge in list_of_links])
                        if mapping[temp.get_url()] == 34480 or mapping[temp.get_url()] == 34479:
                            print(mapping[temp.get_url()], temp.get_url(), list_of_links)
                        # print([(doc_id, final_edge)for final_edge in list_of_links])
    return graph
def get_all_sublinks(root):
    all_links = []
    for i in root.xpath('/html')[0].getiterator('a'):
        url_dict = i.attrib
        if 'href' in  url_dict:
            if url_dict['href'] in mapping:
                all_links.append(mapping[url_dict['href']])
    return all_links


if __name__ == "__main__":
    G = create_graph()
    # pos = nx.spring_layout(G)
    # nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),  node_size = 500)
    # nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='r', arrows=True)
    # nx.draw_networkx_labels(G, pos)
    # plt.show()
    page_rank = nx.pagerank(G)
    with open("indexes/pagerank.txt", "w+") as ranks:
        ranks.write(str(page_rank))


