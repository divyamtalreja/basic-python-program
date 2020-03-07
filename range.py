def range1(n,low,high):
    set=False
    for i in range(low,high+1):
        if (i==n):
          set=True
        elif(n==low):
           set=True
        elif(n==high):  
           set=True
        
    if (set==True):
          print("in range")
    else:       
        print("not in range")
    
    
    
range1(1,10,15)    