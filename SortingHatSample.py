import collections, random

houseList = ["1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4"]
pickList = []

# will replace this with "button press action"
for i in range(15):
   if not pickList:
      # rebuild pickList by pre-randomizing the list
      pickList = random.sample(houseList, k=12)
   
   # pick a house by removing one from list
   print ("Pick:", pickList.pop() )
            
   print (pickList)


