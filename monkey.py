i=0
def go(x,y):
 global i
 i+=1
 print(f"step: {i}, monkey slave {x} Go to {y}")
def move(x,y):
 global i
 i+=1
 print(f"step: {i}, monkey take the box from {x} deliver to {y}")
def climb():
 global i
 i+=1
 print(f"step: {i}, Monkey climbs up the box")
def get():
 global i
 i+=1
 print(f"step: {i}, Monkey picked a banana")

m=input("Enter monkey's location: ")
b=input("Enter banana's location: ")
x=input("Enter box's location: ")
print("The steps are as follows:")
go(m,x); move(x,b); climb(); get()
