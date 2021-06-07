import time
from timeit import default_timer as timer
# import Hardware

"""
    Sequential Batch Reactor, 8 channel relay, anaerobic fermenter = coupled

"""

# Default starting stages with MAX = 10 stages
# This is basically the spreadsheet. index = rows(1-10), (stage,stage mode, time) = cols(1,2,3)
# IMPORTANT: IF THERE IS NO Stage just set "stage": NONE , "stage mode" = NONE, "time " = NONE
stages = [{
    "stage": 1,
    "stage mode": "n2",
    "time": 50
},
    {
    "stage": 2,
    "stage mode": "air",
    "time": 100
},
    {
    "stage": 3,
    "stage mode": "n2",
    "time": 144
},
    {
    "stage": 4,
    "stage mode": "still",
    "time": 122
},
    {
    "stage": 5,
    "stage mode": "still",
    "time": 1332
},
    {
    "stage": 6,
    "stage mode": "still",
    "time": 1
},
    {

    "stage": 7,
    "stage mode": "effluent",
    "time": 233
}, {

    "stage": 8,
    "stage mode": "influent",
    "time": 1000
},
    {

    "stage": 9,
    "stage mode": "effluent",
    "time": 1111
},
    {

    "stage": None,
    "stage mode": None,
    "time": None
}]

# List of possible stageModes
stageModes = ["n2", "air", "fermN2", "influent",
              "effluent", "fermenter", "still"]
# Relay1
# RELAY_12 = Hardware.Relay(12, False)  # n2
# RELAY_13 = Hardware.Relay(13, False)  # air
# RELAY_14 = Hardware.Relay(1, False)  # fermenter_n2

# ph_sensor = PHSensor(....)

# IN5 = Hardware.Relay(17, False)
# IN6 = Hardware.Relay(16, False)
# IN7 = Hardware.Relay(7, False)

# Stepper1Pins = [IN5] # Stepper 1 = influent
# Stepper2Pins = [IN6] # Stepper 2 = effluent
# Stepper3Pins = [IN7] # Stepper 3 = into anaero fermenter


# stepper sequence, as shown in manufacturers datasheet
Seq = [[1, 0]]

# Define pin functions


def ListLength():
    i = 0
    for step in stages:
        if(step["stage"] == None):
            break
        i += 1
    return i


def TotalTime(startStage):
    sum = 0
    for step in stages:
        try:
            if(int(startStage) <= step["stage"]):
                sum = sum + step["time"]
        except:
            break
            pass
            # if None it just goes here.
    return sum


# def N2(onOrOff):
#     if(onOrOff == "on"):
#         # RELAY_12.on()
#         pass
#     elif(onOrOff == "off"):
#         # RELAY_12.off()
#         pass


# def Air(secondsDuration):
#     print("air turned on for ", secondsDuration)
#     # RELAY_13.on()
#     time.sleep(secondsDuration)
#     # RELAY_13.off()


# def FermN2(secondsDuration):
#     print("N2 for anaerobic fermenter turned on for ", secondsDuration)
#     # RELAY_14.on()
#     time.sleep(secondsDuration)
#     # RELAY_14.off()


def Stepper(secondsDuration, inOut):
    start = timer()

    print("Stepper duration", secondsDuration,
          " direction ", inOut, " starting time:", start)

    if inOut == "in":
        # StepPins = Stepper1Pins

        pass
    elif inOut == "out":
        # StepPins = Stepper2Pins

        pass
    else:
       # StepPins = Stepper3Pins

        pass

    # Variable Declarations.
    StepCount = len(Seq)
    StepDir = 1  # Set to 1  for clockwise, -1  for anti-clockwise
    waitTime = 10
    StepCounter = 0

    while True:

        #print("step counter:", StepCounter, " line:", Seq[StepCounter])
        for pin in range(0, 1):
            # xpin = StepPins[pin]
            pass
            if Seq[StepCounter][pin] != 0:
                # xpin.on()
                pass
            else:
                # xpin.off()
                pass

        StepCounter += StepDir
        print("Next Line:", StepCounter)

        if (StepCounter >= StepCount):
            StepCounter = 0
        if (StepCounter < 0):
            StepCounter = StepCount+StepDir

        time.sleep(waitTime)
        # find how long it has been running
        end = timer()
        timeRunningSeconds = end - start
        print("duration in stepper:", timeRunningSeconds)

        if timeRunningSeconds > secondsDuration:
            break


# def Still(secondsDuration):
#     print("Resting for ", secondsDuration)
#     time.sleep(secondsDuration)


def TurnOnStage(stageMode):
    if(stageMode == "n2"):
        # RELAY_12.on()
        print("n2 on")
        pass

    elif(stageMode == "air"):
        # RELAY_13.on()
        print("air on")
        pass
    elif(stageMode == "fermN2"):
        # RELAY_14.on()
        print("fermN2 on")
        pass
    elif(stageMode == "influent"):
        # Stepper(in)
        print("influent on")

        pass
    elif(stageMode == "effluent"):
        # Stepper(out)
        print("effluent on")

        pass
    elif(stageMode == "fermenter"):
        #  Stepper(None)
        print("fermenter on")

        pass
    elif(stageMode == "still"):
        # Do nothing --- Wait
        print("still on")

        pass
    else:
        # Error
        pass


def TurnOffStage(stageMode):
    if(stageMode == "n2"):
        # RELAY_12.off()
        print("n2 off")
        pass

    elif(stageMode == "air"):
        # RELAY_13.off()
        print("air off")
        pass
    elif(stageMode == "fermN2"):
        # RELAY_14.off()
        print("fermN2 off")
        pass
    elif(stageMode == "influent"):
        # Stepper(in)
        print("influent off")

        pass
    elif(stageMode == "effluent"):
        # Stepper(out)
        print("effluent off")

        pass
    elif(stageMode == "fermenter"):
        #  Stepper(None)
        print("fermenter off")

        pass
    elif(stageMode == "still"):
        # Do nothing --- Wait
        print("still off")

        pass
    else:
        # Error
        pass


# def RunCycle():
#     # step -> {"stage": int, "_" = int}

#     for step in stages:
#         print("stage:", step["stage"])

#         if step["stage mode"] == "n2":
#             N2(step["time"])

#         elif step["stage mode"] == "air":
#             Air(step["time"])

#         elif step["stage mode"] == "fermN2":
#             FermN2(step["time"])

#         elif step["stage mode"] == "influent":
#             Stepper(step["time"], "in")

#             # turn off
#             for pin in range(0, 1):
#                 # xpin = Stepper1Pins[pin]
#                 # xpin.off()
#                 pass

#         elif step["stage mode"] == "still":
#             Still(step["time"])

#         elif step["stage mode"] == "effluent":
#             Stepper(step["time"], "out")

#             # turn off
#             for pin in range(0, 1):
#                 # xpin = Stepper2Pins[pin]
#                 # xpin.off()
#                 pass

#         elif step["stage mode"] == "fermenter":
#             Stepper(step["time"], None)

#             # turn off
#             for pin in range(0, 1):
#                 # xpin = Stepper3Pins[pin]
#                 # xpin.off()
#                 pass

#         else:
#             print("error", print(step))
