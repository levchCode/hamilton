# hamilton

Hamiltonians to QUBO written in Python


# Get Started

Get you formulation and just plug it in to hamilton.generate() function. Make sure it starts with x0!

```
import hamilton

#A 2x2 assignment problem
f = "1*(5*x0+6*x1+8*x2+10*x3)+900(1-(x0+x2))**2+900(1-(x1+x3))**2+900(1-(x0+x1))**2+900(1-(x2+x3))**2"

qubo = hamilton.generate(f)

#Returns this qubo (qubo itself, max_index for triple product cases)
({'qubo': [
{'index': [0], 'value': '-1795'},
{'index': [1], 'value': '-1794'},
{'index': [2], 'value': '-1792'},
{'index': [3], 'value': '-1790'},
{'index': [0, 1], 'value': '1800'},
{'index': [0, 2], 'value': '1800'},
{'index': [1, 3], 'value': '1800'},
{'index': [2, 3], 'value': '1800'}
],
'p': 'p qubo 0 4 4 4'}, 0)

```

##Dealing with triples
Coming soon!
