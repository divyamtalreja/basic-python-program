try:
    a=5
    b=0
    c=a/b
    
except ZeroDivisionError:
    print("please check operations again")
    
finally:
    print("all done")