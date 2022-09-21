import tkinter
from tkinter import *  # tkinter used to make new windows
import networkx as nx  # library used for creating and drawing graphs
import matplotlib.pyplot as plt  # used for plotting our graph, could be used to change axes, include subplots, etc.


def run_algorithm(dSeq):
    """ This function runs the Havel-Hakimi algorithm, which determines if a degree sequence (input parameter dSeq)
     is graphical. If the sequence is graphical, then the create_graph() function is called and a new window informs
     the user. Otherwise, a new window informs the user that the sequence is not graphical.
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
    """ This function initialises a networkx Graph object which has the nodes and edges defining a graph
    as its properties. It then uses the degree sequences given by the Havel-Hakimi algorithm to generate and display
    graphs with those degree sequences.
    """
    G = nx.Graph()
    graphs = []
    # loop adds nodes for each 0/entry in final step of Havel-Hakimi
    for i in range(1, len(degreeRecord[-1]) + 1):
        G.add_node(i)
    graphs.append(G.copy())  # a list is used to store the graph corresponding to each step of the algorithm
    # .copy() is used as assignment statements create bindings between target and object in python

    numSteps = len(degreeRecord[0]) - len(degreeRecord[-1])  # calculating number of steps of algorithm that were used
    for j in range(1, numSteps + 1):  # add a node for each step backwards we take
        G.add_node(j + 2)
        newNodeDegree = degreeRecord[-1 - j][0]
        for k in range(0, newNodeDegree):  # for the required degree of that node, add edges
            G.add_edge(j + 2, k + 1)
            """edges add to nodes in order of labelling, e.g. if we add node labelled 3 
            with degree of 2, then it will first be made adjacent to node labelled 1 and then be made adjacent to 
            node labelled 2"""
            graphs.append(G.copy())

    for g in range(0, len(graphs)):
        plt.figure(g + 1)
        nodePos = nx.spring_layout(
            graphs[-g - 1])  # issue with layout here, how to keep consist node positioning between graphs?
        nx.draw(graphs[-g - 1], with_labels=True, pos=nodePos)
    plt.show()


def create_new_window(titleText, degreeRecord, isGraphical):
    """Creates a window  using tkinter which tells the user whether the inputted degree sequence is graphical or not.
    Also uses degreeRecord to display the inputted degree sequence.
    """
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
