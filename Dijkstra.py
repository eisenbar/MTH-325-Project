def infty(graph):
    total = 0
    for node in graph:
        for relation in graph[node]:
            total += (relation[1])
    total = total/2+1
    return (int(total))



def initial(graph):
    start = {}
    for node in graph:
        if node == "A":
            start[node] = 0
        else:
            start[node] = infty(graph)
    return (start)



def find_min(color, queue):
    lightest_node = 10000
    pick_one = {}
    for node in color:
        if node in queue:
            if color[node] < lightest_node:
                lightest_node = color[node]
    for node in color:
        if color[node] == lightest_node and len(pick_one) < 1:
            pick_one[node] = color[node]
    for node in pick_one:
        return(node)


#testing for first 3 parts
graph = {"A":[["B",10],["D",5]], "B":[["A",10], ["C",5]], "C":[["B",5],["D",15]], "D":[["C",15], ["A",5]]}
color = {"A":0, "B":10, "C":10, "D":15}
queue = ["B", "C", "D"]
print (infty(graph))
initial(graph)
find_min(color, queue)


def dijkstra(graph):

    s = initial(graph)

    for key in graph:
        for vertex in graph[key]:
            if s[key] + vertex[1] < s[vertex[0]]:
                s[vertex[0]] = s[key] + vertex[1]
    print(s)
    return s


# testing for part 4
g = {"A": [["B", 10], ["D", 5]], "B": [["A", 10], ["C", 5]], "C": [["B", 5], ["D", 15]], "D": [["C", 15], ["A", 5]]}
dijkstra(g)

def isConnected(graph):
    diestra = dijkstra(graph)
    max = infty(graph)

    for i in diestra:
        if diestra[i] >= max:
            return False

    return True

