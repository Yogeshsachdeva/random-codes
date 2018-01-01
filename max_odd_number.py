x= int(input())
y= int(input())
z= int(input())
l=[x,y,z]
if x%2==0 and y%2==0 and z%2==0:
    print("no number is odd")
else:
    print(max(list(filter(lambda x:x%2, l))))
    