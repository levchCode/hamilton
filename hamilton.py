from itertools import groupby
import sympy
import re


def filtertriples(formula, max_index):
    temp = max_index

    l = re.split('([+-]?\s?(?:[^+-]*))', formula)
    l = list(filter(None, l))

    for i in range(len(l)):
        xs = []
        terms = l[i].split("*")

        for j in terms:
            if j.startswith("x"):
                xs.append(j)

            if len(xs) == 3:
                l[i] = terms[0] + "*(x" + str(max_index) + "*" + xs[2] + " + 100*(3*x" + str(max_index) + " + " + xs[
                    0] + "*" + xs[1] + " - 2*x" + str(max_index) + "*" + xs[0] + " - 2*x" + str(max_index) + "*" + xs[
                           1] + "))"
                max_index += 1

    f = ''.join(l)

    return f, max_index - temp


def generate(formula, max_index=0):
    qubo = []
    nodes = 0
    couplers = 0
    a_v = 0

    if max_index != 0:
        print("Looking for triples...")
        formula, a_v = filtertriples(str(sympy.poly(formula).as_expr()), max_index)

    print("Generating...  AUXes - " + str(a_v))

    qb = sympy.poly(formula)

    for key, value in qb.as_dict().items():

        if 2 in key:
            indices = [l for l, x in enumerate(key) if x == 2]
            if {"index": indices, "value": value} not in qubo:
                qubo.append({"index": indices, "value": value})

        if 1 in key:
            indices = [k for k, y in enumerate(key) if y == 1]
            qubo.append({"index": indices, "value": value})

    qubo = [{'index': k, 'value': str(sum(int(d['value']) for d in ds))} for k, ds in
            groupby(sorted(qubo, key=lambda d: d['index']), lambda d: d['index'])]

    for q in qubo:
        if len(q["index"]) == 1:
            nodes += 1
        else:
            couplers += 1

    print("Done generating")
    return {"qubo": sorted(qubo, key=lambda d: len(d['index'])),
            "p": "p qubo 0 " + str(nodes) + " " + str(nodes) + " " + str(couplers)}, a_v
