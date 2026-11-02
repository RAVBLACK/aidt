def toh(n,a,b,c):
    if n==1: print("Move disk 1 from source",a,"to destination",c); return
    toh(n-1,a,c,b)
    print("Move disk",n,"from source",a,"to destination",c)
    toh(n-1,b,a,c)

n=4
toh(n,'A','B','C')
