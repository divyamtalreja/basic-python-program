import math
class line:
    
    def __init__(self,cor1,cor2):
        self.cor1=cor1
        self.cor2=cor2
    def distance(self):
        distance=0
        distance=math.sqrt(((cor2[0]-cor1[0])**2)+((cor1[1]-cor2[1])**2))
        print(distance)
    def slope(self):
        slope=0
        slope=(cor2[1]-cor1[1])/(cor2[0]-cor1[0])
        print(slope)
         






cor1=[3,2]
cor2=[8,10]
cr=line(cor1,cor2)
cr.slope()
cr.distance()