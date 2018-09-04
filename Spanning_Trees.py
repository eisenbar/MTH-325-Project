from copy import deepcopy


def edge_get(graph):

    order = find_mins(graph)

    for pair in order:
        for i in pair:
            for g in pair:
                if [i, g] in order and [g, i] in order:
                    a = order.index([i, g])
                    del order[a]

    return order


def find_mins(graph):

    weights = []
    order = []

    for key in graph:
        for vertex in graph[key]:
           if vertex[1] not in weights:
               weights.append(vertex[1])

    weights = sorted(weights)

    for w in weights:
        for key in graph:
            for vertex in graph[key]:
                if w == vertex[1]:
                    order.append([key, vertex[0]])

    return order


def list_join(lst, elt1, elt2):

    copy = deepcopy(lst)

    #finds elt1 and elt2 in lst and joins the two lists together
    for i in lst:
        if elt1 in i:
            pos1 = lst.index(i)
        if elt2 in i:
            pos2 = lst.index(i)

    if pos2 != pos1:
        copy[pos1] += copy[pos2]
        del copy[pos2]

    return copy


def min_kruskal(graph):
    kruskal = edge_get(graph)
    del kruskal[len(kruskal)-1]
    return kruskal


def smallNs(graph, vertex, edge):
    smallest = ["", -1]
    for v in graph[vertex]:
        if smallest[1] < 0 or smallest[1] > v[1]:
            if [vertex, v[0]] not in edge and [v[0], vertex] not in edge:
                smallest = v

    return smallest

def min_prim(graph):
    prim = []
    start = ["A"]

    while True:
        smallEs = []
        smallest = ["", "", -1]

        for vertex in start:
            edge = smallNs(graph, vertex, prim)
            smallEs.append([vertex, edge[0], edge[1]])

        for edge in smallEs:
            if smallest[2] < 0 or smallest[2] > edge[2]:
                if [edge[0], edge[1]] not in prim and [edge[1], edge[0]] not in prim:
                    smallest = edge

        prim.append([smallest[0], smallest[1]])
        if smallest[0] in start:
            start.append(smallest[1])
        else:
            start.append(smallest[0])

        if len(start) >= len(graph):
            break

    return prim


g = {'A': [['B', 10], ['D', 5]], 'B': [['A', 10], ['C', 5]], 'C': [['B', 5], ['D', 15]], 'D': [['C', 15], ['A', 5]]}
ls = [['A', 'B'], ['C'], ['D'], ['E', 'F']]

print("Edge get: " + str(edge_get(g)))
print("List join 1: " + str(list_join(ls, 'A', 'D')))
print("List join 2: " + str(list_join(ls, 'A', 'B')))
print("Kruskal: " + str(min_kruskal(g)))
print("Prim: " + str(min_prim(g)))
