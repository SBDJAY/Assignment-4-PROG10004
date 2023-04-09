'''This is code for error handeling for numOfsensors in createsensors def and the id name variable that goes in the list'''



# listSensors = []
    
#     def createSensors():
#         numOfSensors = int(input('Enter the number of sensors: '))  #Takes the integer input for the Number of sensors
#         index = 0
#         #while numOfSensors == True:     #While Loop to check if numOfSensors is an int value (If true then will ask for the Sensor ID if false it will return the question)
#             #if numOfSensors == int:
#                 #------------------------------------------------------------------------
#         while index < numOfSensors:     #While loop to check if Wireless.id from WirelessNetwork Class(Module) is an Integer value (if true then appends listSensors from the Application Class, and a)
#             WirelessNetwork.id = str(input("Enter the Sensor ID: "))
#                     #while WirelessNetwork.id == True:
#                         #if WirelessNetwork.id == str:
#             Application.listSensors.append (WirelessNetwork.id)
#             index += 1
#                 #else:
#                     #print('This is an invalid entry for sensor Id!')
#                 #-------------------------------------------------------------------------
#             #else:
#                 #print('This is an invalid entry for the number of sensors!')
        
#         print(Application.listSensors)

# x=int(input("enter the size of list"))
# y= int(input("enter the size of sublist"))
# list1=[]
# sublist=[]
# for i in range(x):
#     for j in range(y):
#         sublist.append(input())
#     list1.append(sublist)
#     sublist=[]
# print (list1)

class Application(WirelessNetwork):
    #Attributes
    listSensors = []
    
    def createSensors():
        numOfSensors = int(input('Enter the number of sensors: '))  #Takes the integer input for the Number of sensors
        #index = 0
        for WirelessNetwork.id in range(numOfSensors):     # For loop to ask sensor ID from the previous input of how many sensors there are 
            WirelessNetwork.id = str(input("Enter the Sensor ID: ")) 
            Application.listSensors.append (WirelessNetwork.id)
            #index += 1 
            for numOfNeighbours in (WirelessNetwork.id): #For loop to ask for Number of Neighbours for each sesnor ID / Number of sensors that was inputed
                numOfNeighbours = int(input('Enter the number of neighbours: '))
                
            
                for neighbourName in range (numOfNeighbours): #for loop to asks the name of each link / Neighbour sensor for how many neighbours that were inputed
                    neighbourName = str(input("Enter the Neighbour ID: "))
                    distance = int(input('Enter the Distance to '+(WirelessNetwork.id)+': '))
                    WirelessNetwork.link.append(neighbourName)
                    WirelessNetwork.link.append(distance)
                    #for WirelessNetwork.link in (WirelessNetwork.id):
                        
            #Asks user the Oxygen Level and Temperature fro the Sensor after other loops are completed
            WirelessNetwork.oxygenLevel = int(input('Enter the Oxygen level in %: '))
            WirelessNetwork.temperature = float(input('Enter the temperature measurement: '))

            Application.listSensors.append(WirelessNetwork.link)        

        
        #print(Application.listSensors)
        print(WirelessNetwork.link)