import random
def randdom(low,high,n):
   for i in range(0,n):
       in1= random.randint(low,high)
       yield in1
       
for i in randdom(1000,5000,20):
      print(i)
      