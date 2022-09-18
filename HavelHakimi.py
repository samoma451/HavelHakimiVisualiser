import networkx as nx
import matplotlib.pyplot as plt

def run_algorithm(dSeq):
    degreeRecord = []
    for i in range(0, len(dSeq)-1):
        dSeq.sort(reverse=True)
        degreeRecord.append(list(dSeq))
        print(dSeq)
        count = dSeq[0]
        print(count)
        if count == 0:
            break
        dSeq.pop(0)
        if len(dSeq) < count:
            break
        for j in range(0,count):
            dSeq[j] = dSeq[j] - 1
            print(dSeq)

    if dSeq[0] == 0:
        print("graph valid")
        create_graph(degreeRecord)
    else:
        print("graph invalid")

def create_graph(degreeRecord, seed = 2022):
    G = nx.Graph()
    for i in range(1, len(degreeRecord[-1]) + 1):
        G.add_node(i)
        #print(G.nodes())
    nx.draw(G)
    plt.show()

testSeq = [4,3,4,3,2]
run_algorithm(testSeq)