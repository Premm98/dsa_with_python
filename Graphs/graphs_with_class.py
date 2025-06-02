class Graph():

    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def print(self):
        connection = [node.value for node in self.neighbours]
        print(f'Node {self.value} is connected to {connection}')

A = Graph('A')
B = Graph('B')
C = Graph('C')
D = Graph('D')
E = Graph('E')

A.neighbours.append(B)
B.neighbours.append(A)

A.neighbours.append(C)
C.neighbours.append(B)

C.neighbours.append(D)
D.neighbours.append(C)

D.neighbours.append(E)
E.neighbours.append(B)

A.print()
B.print()
