import json
import time
from timeit import default_timer as timer
import Hardware


"""
    Sequential Batch Reactor, 8 channel relay, anaerobic fermenter = coupled
   
"""

#Relay1
RELAY_12  = Hardware.Relay(12, False) #n2
RELAY_13  = Hardware.Relay(13, False) #air
RELAY_14  = Hardware.Relay(1, False) #fermenter_n2

#Stepper 1 = influent
IN5 = Hardware.Relay(17, False)
Stepper1Pins=[IN5]

#Stepper 2 = effluent
IN6  = Hardware.Relay(16, False)
Stepper2Pins=[IN6]

#Stepper 3 = into anaero fermenter
IN7  = Hardware.Relay(7, False)
Stepper3Pins=[IN7]

# stepper sequence, as shown in manufacturers datasheet
Seq = [[1,0]]

#Define pin functions
def n2(secondsDuration):  
    print ("N2 turned on for ",secondsDuration)
    RELAY_12.on()
    time.sleep(secondsDuration)
    RELAY_12.off()

def air(secondsDuration):  
    print ("air turned on for ",secondsDuration)
    RELAY_13.on()
    time.sleep(secondsDuration)
    RELAY_13.off()

def fermN2(secondsDuration):
    print ("N2 for anaerobic fermenter turned on for ",secondsDuration)    
    RELAY_14.on()
    time.sleep(secondsDuration)
    RELAY_14.off()
    
def stepper(secondsDuration, inout):
    start = timer()
    StepCount = len(Seq)
    StepDir = 1 # Set to 1  for clockwise, -1  for anti-clockwise
    WaitTime = 10
    StepCounter = 0
    print ("Stepper duration",secondsDuration ," direction ", inout, " starting time:",start )     
   
    if inout=="in":
        StepPins=Stepper1Pins
    elif inout=="out":
        StepPins=Stepper2Pins
    else:
        StepPins=Stepper3Pins
        
    while True:
        print ("step counter:",StepCounter, " line:", Seq[StepCounter])
    
        for pin in range(0, 1):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin]!=0:
                xpin.on()
            else:
                xpin.off()
 
        StepCounter += StepDir
        print("Next Line:",StepCounter )
        if (StepCounter>= StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount+StepDir
        
        time.sleep(WaitTime)
        #find how long it has been running
        end=timer()
        timeRunningSeconds=end-start
        print("duration in stepper:",timeRunningSeconds)

        if timeRunningSeconds>secondsDuration:
            break

    
def still(secondsDuration):
    print ("Resting for ",secondsDuration)    
    time.sleep(secondsDuration)    

#Define Cycle
def main():

    with open('normal.json','r') as config_file:
        data=json.load(config_file)

    while True:
        for step in data['stages']:
            #print ("step:", step)
            for key,value  in step.items():
                
                if str(key) == "stage":
                    print("stage:",value)
                elif str(key) == "n2":
                    n2(value)
                elif str(key) == "air":
                    air(value) 
                elif str(key) == "fermN2":
                    fermN2(value) 
                elif str(key) == "influent":
                    stepper(value,"in")
                    #turn off 
                    for pin in range(0, 1):
                        xpin = Stepper1Pins[pin]
                        xpin.off()
                elif str(key) == "still":
                    still(value)    
                elif str(key) == "effluent":
                    stepper(value,"out") 
                    #turn off 
                    for pin in range(0, 1):
                        xpin = Stepper2Pins[pin]
                        xpin.off()
                elif str(key) == "fermenter":
                    stepper(value,"fermenter") 
                    #turn off 
                    for pin in range(0, 1):
                        xpin = Stepper3Pins[pin]
                        xpin.off()
                else:
                    print("error in config:",value)      
   
if __name__ == '__main__':
    main()
