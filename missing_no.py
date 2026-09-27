# TO FIND THE SMALLEST MISSING NUMBER
# input 1 2 4 5
# output 3
number=set(map(int,input().split()))
smallest=1 
while smallest in number:
    smallest+=1 
print(smallest)
