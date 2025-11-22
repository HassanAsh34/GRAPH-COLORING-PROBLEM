
import random
import time


import matplotlib.colors as colorlib

import Node as n

import BackTracking as b

# # def coloring(solution,lcolor,i,lnodes):
# #     if i == len(lnodes):
# #         solution.append([node.color for node in lnodes])
# #         return
# #         # fillColor(node[0],lcolor)
# #     node = lnodes[i]
# #     for color in lcolor:
# #         if(node.isSafe(color)):
# #             node.color = color
# #             coloring(solution,lcolor,i+1,lnodes)
# #             node.color = "" #for backtracking
#
# def coloringWithCanonicalOrder(solution,solsorted_set,lcolor,i,lnodes):
#     if i == len(lnodes):
#         sol = [node.color for node in lnodes]
#         sortedsol = sorted(sol)
#         # res =
#
#         if tuple(sortedsol) not in solsorted_set:
#             solution.append(sol)
#             solsorted_set.add(tuple(sortedsol))
#         return
#     if len(solution) >= 5000:
#         return
#         # fillColor(node[0],lcolor)
#     node = lnodes[i]
#     for cid, color in enumerate(lcolor):
#         if(node.isSafeCanonical(cid)):
#             node.color = cid
#             coloringWithCanonicalOrder(solution,solsorted_set,lcolor,i+1,lnodes)
#             node.color = -1 #for backtracking
#
# def getSolutions(lnodes,lcolor):
#     Solutions = list()
#     solsorted_set = set()
#     nodes = copy.deepcopy(lnodes)
#     # for c in lcolor:
#         # nodes[0].color = c
#         # solution = list()
#     coloringWithCanonicalOrder(solution=Solutions,solsorted_set= solsorted_set,lcolor=lcolor, lnodes=nodes, i=0)
#         # Solutions.append((c,solution))
#     return Solutions
#
#
# def evaluateSolutions(solutions):
#     evaluatedSols= list()
#     for sol in solutions:
#         chromaticnum = len(set(sol))
#         evaluatedSols.append((chromaticnum,sol))
#     evaluatedSols.sort(key= lambda x: x[0])
#     return evaluatedSols


# def fillColor(node,lcolor):
#     sol = []
#     if node.color != "":
#         sol.append(node.color)
#     else:
#         color = random.choice(lcolor)
#         if node.isSafe(color):
#             node.color = color
#             for n in node.edges:
#                 if n.Id > node.Id:





# def printGraph(g,optimal,colors):
#     pos = nx.spring_layout(g)
#     edge_labels = {(u, v): f"{u}-{v}" for u, v in g.edges}
#     # if
#     if optimal != None:
#         optimal = random.choice(optimal)
#         color = []
#         for i in optimal:
#             color.append(colors[i])
#         nx.draw(g,node_color= color, pos=pos, with_labels=True, node_size=800, font_weight="bold")
#
#
#     else:
#         nx.draw(g,pos=pos, with_labels=True, node_size=800, font_weight="bold")
#
#     if edge_labels.items():
#         print(edge_labels)
#         nx.draw_networkx_edge_labels(g,pos=pos,edge_labels=edge_labels)
#     plt.show()
#
# def addEdges(g,nodes,edges):
#     try:
#         a, b = map(int, edges.split())
#         if a in g.nodes and b in g.nodes:
#             t = tuple(sorted((a,b)))
#             if t in g.edges:
#                 print("edge already exists")
#             else:
#                 g.add_edge(a, b)
#                 n1 = n2  = None
#                 for node in nodes:
#                     if(node.Id == a or node.Id == b):
#                         if n1 == None:
#                             n1 = node
#                         elif n2 == None and n1 != None:
#                             n2 = node
#                         else:
#                             continue
#                 if n1 is not None and n2 is not None:
#                     if isinstance(n1, Node) and isinstance(n2, Node):
#                         n1.addEdge(n2)
#                         n2.addEdge(n1)
#                         print(f"Connected node {n1.Id} with {n2.Id}")
#                     else:
#                         print("Something went wrong with IDs or node lookup.")
#                 else:
#                     print("something gone wrong with ids")
#         else:
#             print("Invalid node IDs.")
#     except ValueError:
#         print("Enter two numbers separated by a space.")

# class Node:
#     _counter = 0
#
#     def __init__(self,):
#         Node._counter +=1
#         self.Id = Node._counter
#         self.edges = []
#         # self.color = ""
#         self.color = -1
#     def addEdge(self,node):
#         self.edges.append(node)
#         # shape = "Circle"
#     def isSafe(self,color):
#         for node in self.edges:
#             if(color.lower() == node.color.lower()):
#                 return False
#         return True
#
#     def isSafeCanonical(self,color):
#         for node in self.edges:
#             if(color == node.color):
#                 return False
#         return True






g = n.nx.Graph()

nodes = list()

nodesCount = int(input("enter number of nodes"))

colorCount = int(input("enter number of colors"))

colors = random.sample([
     c for c in list(colorlib.CSS4_COLORS.keys())
    if not any(shade in c for shade in ['light', 'dark', 'medium'])
],colorCount)



optimal = None

print(colors)

for i in range(nodesCount):
    node = n.Node()
    nodes.append(node)
    g.add_node(node.Id)

op = 0
while True:
    try:
        op = int(input("""
        1- display
        2- add edges
        3- add node
        4 - solve coloring
        5 - exit
        """))
    except:
        print("invalid operation")

    if (op == 1):
            n.printGraph(g,optimal,colors)
    elif (op == 2):
        edge_input = ""
        while edge_input.lower().strip() != "done":
            edge_input = input("Enter two nodes to connect (e.g. 1 2), or 'done' to finish: ")
            if edge_input.lower().strip() != "done":
                n.addEdges(g, nodes, edge_input)
    elif (op == 3):
        node = n.Node()
        nodes.append(node)
        optimal = None
        g.add_node(node.Id)
    elif(op == 4):
        solutions = b.getSolutions(lnodes=nodes,lcolor=colors)
        if not solutions:
            print("current number of colors is insufficient")
            addcolor = input("do yo want to add a new color? y/n")
            if(addcolor.lower().strip() == "y"):
                color = random.choice(list(colorlib.CSS4_COLORS.keys()))
                while color in colors:
                    color = random.choice(list(colorlib.CSS4_COLORS.keys()))
                colors.append(color)
        else:
            # print(solutions)
            start = time.time()
            evsols = b.evaluateSolutions(solutions)
            minnum = evsols[0][0]
            print(evsols)
            optimal = [sols for cnum, sols in evsols if cnum == minnum ]
            print(f"chromatic number is {minnum} and {len(optimal)} optimal solutions found")
            end = time.time()
            print(f"{end - start:.6f} seconds")
            # print(optimal)
            # print(optimal[0])
    elif(op == 5):
        print("exiting")
        exit()
    else:
        print("invalid operation")





