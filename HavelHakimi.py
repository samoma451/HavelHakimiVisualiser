import networkx as nx
import matplotlib.pyplot as plt


def run_algorithm(dSeq):
    degreeRecord = []
    for i in range(0, len(dSeq) - 1):
        dSeq.sort(reverse=True)
        degreeRecord.append(list(dSeq))
        print(dSeq)
        count = dSeq[0]
        if count == 0:
            break
        dSeq.pop(0)
        if len(dSeq) < count:
            break
        for j in range(0, count):
            dSeq[j] = dSeq[j] - 1

    if dSeq[0] == 0:
        print("graph exists")
        create_graph(degreeRecord)
    else:
        print("graph does not exist")


def create_graph(degreeRecord):
    G = nx.Graph()
    graphs = []
    for i in range(1, len(degreeRecord[-1]) + 1):
        G.add_node(i)
    graphs.append(G.copy())

    numSteps = len(degreeRecord[0]) - len(degreeRecord[-1])
    for j in range(1, numSteps+1):
        G.add_node(j + 2)
        newNodeDegree = degreeRecord[-1 - j][0]
        for k in range(0, newNodeDegree):
            G.add_edge(j + 2, k+1)
        graphs.append(G.copy())

    for g in range(0, len(graphs)):
        plt.figure(g + 1)
        nodePos = nx.spring_layout(graphs[-g-1])#issue with layout here, how to keep consist node positioning between graphs?
        nx.draw(graphs[-g-1],with_labels=True,pos=nodePos)
    plt.show()


testSeq = [4, 3, 4, 3, 2]
run_algorithm(testSeq)
