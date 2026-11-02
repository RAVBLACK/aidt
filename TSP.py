from itertools import permutations

g=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
m=999

for p in permutations([1,2,3]):
    c=g[0][p[0]]+g[p[0]][p[1]]+g[p[1]][p[2]]+g[p[2]][0]
    m=min(m,c)

print("Minimum weight Hamiltonian Cycle:",m)
