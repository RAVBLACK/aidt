g={'A':['B','C'],'B':['D','E'],'C':['F'],'D':[],'E':['F'],'F':[]}
q=['A']; v=[]
while q:
    n=q.pop()
    if n not in v:
        print(n,end=' '); v.append(n)
        q+=g[n][::-1]
