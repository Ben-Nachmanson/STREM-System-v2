import time
from timeit import default_timer as timer
import threading
# import Hardware

"""
    Sequential Batch Reactor, 8 channel relay, anaerobic fermenter = coupled

"""
global State
# Default starting stages
stages = [{
    "stage": 1,
    "stage mode": "n2",
    "time": 400
},
    {
    "stage": 2,
    "stage mode": "influent",
    "time": 300
},
    {
    "stage": 3,
    "stage mode": "n2",
    "time": 100
},
    {
    "stage": 4,
    "stage mode": "still",
    "time": 1300
},
    {
    "stage": 5,
    "stage mode": "air",
    "time": 5700
},
    {
    "stage": 6,
    "stage mode": "still",
    "time": 600
}]

# Relay1
# RELAY_12 = Hardware.Relay(12, False)  # n2
# RELAY_13 = Hardware.Relay(13, False)  # air
# RELAY_14 = Hardware.Relay(1, False)  # fermenter_n2

# IN5 = Hardware.Relay(17, False)
# IN6 = Hardware.Relay(16, False)
# IN7 = Hardware.Relay(7, False)

# Stepper1Pins = [IN5] # Stepper 1 = influent
# Stepper2Pins = [IN6] # Stepper 2 = effluent
# Stepper3Pins = [IN7] # Stepper 3 = into anaero fermenter


# stepper sequence, as shown in manufacturers datasheet
Seq = [[1, 0]]

# Define pin functions


def totalTime(startStage):
    sum = 0

    for step in stages:
        if(int(startStage) <= step["stage"]):
            sum = sum + step["time"]
    return sum


def n2(secondsDuration):
    print("N2 turned on for ", secondsDuration)
    # RELAY_12.on()
    time.sleep(secondsDuration)
    # RELAY_12.off()


def air(secondsDuration):
    print("air turned on for ", secondsDuration)
    # RELAY_13.on()
    time.sleep(secondsDuration)
    # RELAY_13.off()


def fermN2(secondsDuration):
    print("N2 for anaerobic fermenter turned on for ", secondsDuration)
    # RELAY_14.on()
    time.sleep(secondsDuration)
    # RELAY_14.off()


def stepper(secondsDuration, inOut):
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

        print("step counter:", StepCounter, " line:", Seq[StepCounter])
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


def still(secondsDuration):
    print("Resting for ", secondsDuration)
    time.sleep(secondsDuration)


def dictAdjust():
    pass


def runCycle():
    # step -> {"stage": int, "_" = int}

    for step in stages:
        print("stage:", step["stage"])

        if step["stage mode"] == "n2":
            n2(step["time"])

        elif step["stage mode"] == "air":
            air(step["time"])

        elif step["stage mode"] == "fermN2":
            fermN2(step["time"])

        elif step["stage mode"] == "influent":
            stepper(step["time"], "in")

            # turn off
            for pin in range(0, 1):
                # xpin = Stepper1Pins[pin]
                # xpin.off()
                pass

        elif step["stage mode"] == "still":
            still(step["time"])

        elif step["stage mode"] == "effluent":
            stepper(step["time"], "out")

            # turn off
            for pin in range(0, 1):
                # xpin = Stepper2Pins[pin]
                # xpin.off()
                pass

        elif step["stage mode"] == "fermenter":
            stepper(step["time"], None)

            # turn off
            for pin in range(0, 1):
                # xpin = Stepper3Pins[pin]
                # xpin.off()
                pass

        else:
            print("error", print(step))