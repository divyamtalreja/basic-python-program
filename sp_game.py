def spy_game(n):
    for i in range(0,len(n)):
        if (n[i]==0):
            list1=n[i+1:]
            for j in range(0,len(list1)):
                if(n[j]==0):
                    list2=n[j+1:]
                    for k in range(0,len(list2)):
                        if (n[k]==7):
                          print("true")
                          
    print("false")
    
    
  
spy_game([1,2,0,0,7,1,2])  