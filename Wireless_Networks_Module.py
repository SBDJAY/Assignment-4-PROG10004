#-------------------------------------------------
#Daniel Pius
#Tarek El Salti
#April 9 2023
#PROG 10004 PROGRAMING PRINCIPLES
#Wireless Networks Module
#-------------------------------------------------
#Import
import time
#-------------------------------------------------
class WirelessNetwork():
    #constants
    BRAND_NAME = "Cisco brand" 
    ADHOC_Mode = "ON"
    #Attributes
    id = str
    oxygenLevel = int
    temperature = float
    link = []

    def greetMessage():      
        #This Definiition prints out a welcome message and is only called once, contains constants BRAND_NAME and ADHOC_MODE
        print('******************************************************************************')
        time.sleep(1)
        print("Welcome to the company's IoT-Based Health System")
        time.sleep(1)
        print('These are sensors of brand',WirelessNetwork.BRAND_NAME,'and their Ad Hoc Mode is',WirelessNetwork.ADHOC_Mode)
        time.sleep(1)
        print('******************************************************************************') 
