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
    #Attributes
    listSensors = []
    
    def createSensors():
    
        numOfSensors = int(input('Enter the number of sensors: '))  #Takes the integer input for the Number of sensors
           
        #index = 0
        for sensorID in range(numOfSensors):     # For loop to ask sensor ID from the previous input of how many sensors there are 
            sensorID = str(input("Enter the Sensor ID: ")) 
            Application.listSensors.append (sensorID)
            for numOfNeighbours in (sensorID): #For loop to ask for Number of Neighbours for each sesnor ID / Number of sensors that was inputed
                numOfNeighbours = int(input('Enter the number of neighbours: '))
                
            
                for WirelessNetwork.id in range (numOfNeighbours): #for loop to asks the name of each link / Neighbour sensor for how many neighbours that were inputed
                    WirelessNetwork.id = str(input("Enter the Neighbour ID: "))
                    distance = int(input('Enter the Distance to '+(sensorID)+': '))
                    WirelessNetwork.link.append(WirelessNetwork.id)
                    WirelessNetwork.link.append(distance)
                    #for WirelessNetwork.link in (WirelessNetwork.id):
                        
            #Asks user the Oxygen Level and Temperature fro the Sensor after other loops are completed
            WirelessNetwork.oxygenLevel = int(input('Enter the Oxygen level in %: '))
            WirelessNetwork.temperature = float(input('Enter the temperature measurement: '))

            Application.listSensors.append(WirelessNetwork.link)        

        
        print(Application.listSensors)
        print(WirelessNetwork.link)
    
    def findPath(self, graph, _start, end, path=[]):
        self.graph = graph
        self._start = _start
        self.end = end
        self.path = path

        graph = dict(Application.listSensors)
        print(graph)
    
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
Application.findPath