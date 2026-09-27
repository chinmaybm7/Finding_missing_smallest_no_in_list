# TO FIND THE SMALLEST MISSING NUMBER
number=set(map(int,input().split()))
smallest=1 
while smallest in number:
    smallest+=1 
print(smallest)