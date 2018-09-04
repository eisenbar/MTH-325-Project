from copy import deepcopy


def is_reflex(ground, relation):
    count = 0

    for g in ground:
        if [g, g] in relation:
            count += 1

    if count == len(ground):
        return True
    return False


def is_sym(ground, relation):

    r = deepcopy(relation)

    for g in ground:
        for i in ground:
            if [g, i] in r and [i, g] in r:
                r.remove([g, i])
                if g != i:
                    r.remove([i, g])

    if len(r) == 0:
        return True

    return False


def is_antisym(ground, relation):

    for g in ground:
        for i in ground:
            if [g, i] in relation and [i, g] in relation:
                if g != i:
                    return False
    return True


def is_trans(ground, relation):

    r = deepcopy(relation)

    for g in ground:
        for i in ground:
            if [g, i] in r and [i, g] in r:
                if g != i:
                    return False
            for c in ground:
                if [g, i] in r and [i, c] in r and [c, g] in r:
                    if g != c:
                        return False

    return True


def trans_clos(dGraph):

    transClos = {}

    for key in dGraph:
        transClos[key] = dGraph[key]
        for i in dGraph[key]:
            transClos[key] = transClos[key] + dGraph[i]

    for key in transClos:
        transClos[key] = list(set(transClos[key]))

    return transClos


ground1 = ['A', 'B', 'C', 'D', 'E']
ground2 = ['A', 'B', 'C']
relation1 = [['A', 'A'], ['A', 'D'], ['B', 'C'], ['B', 'D'], ['C', 'E'], ['D', 'A'], ['E', 'E']]
relation2 = [['A', 'A'], ['A', 'B'], ['A', 'C'], ['B', 'B'], ['B', 'A'], ['C', 'C'], ['C', 'A']]
grAnti = ['A', 'B', 'C', 'D']
relAnti = [['A', 'A'], ['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'D'], ['C', 'D'], ['C', 'C']]

tclos1 = {'A': ['B'], 'B': ['C'], 'C': ['B'], 'D': ['A', 'C']}
tclos2 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}


print("Reflexive 1: " + str(is_reflex(ground1, relation1)))
print("Reflexive 2: " + str(is_reflex(ground2, relation2)))
print("Sym 1: " + str(is_sym(ground1, relation1)))
print("Sym 2: " + str(is_sym(ground2, relation2)))
print("AntiSym 1: " + str(is_antisym(ground1, relation1)))
print("AntiSym 2: " + str(is_antisym(grAnti, relAnti)))
print("Trans 1: " + str(is_trans(ground1, relation1)))
print("Trans 2: " + str(is_trans(grAnti, relAnti)))
print("Transitive Closure 1: " + str(trans_clos(tclos1)))
print("Transitive Closure 2: " + str(trans_clos(tclos2)))


