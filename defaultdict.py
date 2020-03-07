from collections import defaultdict,namedtuple,timeit
timeit.timeit(d=defaultdict(object))

for items in d:
 print (items)
 dog=namedtuple("dog","age,breed")
 sam=dog(age='2',breed="lab")
 print(sam)