def gensquares(n):
 for i in range(0,n+1):
     yield(i*i)
    
for i in gensquares(10):
    print(i)
    