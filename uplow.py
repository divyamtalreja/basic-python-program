def uplow(s):
    uppercase=0
    lowercase=0
    for i in range(0,len(s)):
        if (s[i].isupper()):
            uppercase=uppercase+1
        elif(s[i].islower()):
             lowercase=lowercase+1
    print(uppercase)
    print(lowercase)
     
     
uplow("The boy is Good")     