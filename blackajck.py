def blackjack(a,b,c):
    if a+b+c<=21:
        print(a+b+c)
    elif (a+b+c)>21:
         if (a==11):
             print ((a+b+c)-10)
         elif(b==11):
              print ((a+b+c)-10)
         elif(c==11):
              print ((a+b+c)-10) 
         else:
             print("bust")
             
blackjack(11,25,5)             