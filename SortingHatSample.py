import collections, random

houseList = ["1", "2", "3", "4", "1", "2", "3", "4", "1", "2", "3", "4"]
pickList = []


#==========================================================================================================
# pickTeam
def pickTeam():
   global pickList
   
   if not pickList:
      # rebuild pickList by pre-randomizing the list
      pickList = random.sample(houseList, k=len(houseList))
   
   # pick a house by removing one from list
   myPick = pickList.pop()
   return myPick


#----------------------------------------------------------------------------------------------------------
# main execution section
# will replace this with "button press action"

print (pickList)
for i in range(15):
   myPick = pickTeam()
   print ("Pick:", myPick )
               
   print (pickList)


