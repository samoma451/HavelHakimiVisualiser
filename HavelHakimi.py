import tkinter
from tkinter import *  # tkinter used to make new windows
import networkx as nx  # library used for creating and drawing graphs
import matplotlib.pyplot as plt  # used for plotting our graph, could be used to change axes, include subplots, etc.


def run_algorithm(dSeq):
    """ This function runs the Havel-Hakimi algorithm, which determines if a degree sequence (input parameter dSeq)
     is graphical. If the sequence is graphical, then the create_graph() function is called and a new window informs the user.
     Otherwise a new window informs the user that the sequence is not graphical.
    """
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
        create_new_window("Congratulations", degreeRecord, TRUE)
        create_graph(degreeRecord)
    else:
        create_new_window("Sorry My Friend", degreeRecord, FALSE)


def create_graph(degreeRecord):
    G = nx.Graph()
    graphs = []
    for i in range(1, len(degreeRecord[-1]) + 1):
        G.add_node(i)
    graphs.append(G.copy())

    numSteps = len(degreeRecord[0]) - len(degreeRecord[-1])
    for j in range(1, numSteps + 1):
        G.add_node(j + 2)
        newNodeDegree = degreeRecord[-1 - j][0]
        for k in range(0, newNodeDegree):
            G.add_edge(j + 2, k + 1)
        graphs.append(G.copy())

    for g in range(0, len(graphs)):
        plt.figure(g + 1)
        nodePos = nx.spring_layout(
            graphs[-g - 1])  # issue with layout here, how to keep consist node positioning between graphs?
        nx.draw(graphs[-g - 1], with_labels=True, pos=nodePos)
    plt.show()


def create_new_window(titleText, degreeRecord, isGraphical):
    win = Tk()
    win.title(titleText)
    win.geometry('500x200+50+50')

    if isGraphical:
        labelText = "Degree Sequence: " + str(degreeRecord[0]) + "\nThat degree sequence is graphical" + \
                    "\nPlease close this window to see how such a graph can be constructed"
    else:
        labelText = "Degree Sequence: " + str(degreeRecord[0]) + "\nThat degree sequence is not graphical"

    tkinter.Label(text=labelText, height=50, font=("Calibri", 12)).pack()

    win.mainloop()


testSeq = [6, 6, 6, 6, 6, 6, 6, 6]
run_algorithm(testSeq)
