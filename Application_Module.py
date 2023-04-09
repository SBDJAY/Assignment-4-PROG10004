#-------------------------------------------------
#Daniel Pius
#Tarek El Salti
#April 9 2023
#PROG 10004 PROGRAMING PRINCIPLES
#Application Module
#-------------------------------------------------
#Import Statements
import time
from Wireless_Networks_Module import WirelessNetwork
#-------------------------------------------------
#Class ----> Variable
WireNet = WirelessNetwork
#-------------------------------------------------
class Application(WirelessNetwork):
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
                    distance = int(input('Enter the Distance to: '))
                    WirelessNetwork.link.append(neighbourName)
                    WirelessNetwork.link.append(distance)
            Application.listSensors.append(WirelessNetwork.link)        

        
        print(Application.listSensors)

    def findPath(self, graph, _start, end, path=[]):
        self.graph = graph
        self._start = _start
        self.end = end
        self.path = path
        pass
    def findMaxReading(self, first, second):
        self.first = first
        self.second = second

        pass

    def start():
        WireNet.greetMessage()
#-------------------------------------------------
#Calling Classes
Application.start()
Application.createSensors()