import json
import time
from timeit import default_timer as timer
# import Hardware

"""
    Sequential Batch Reactor, 8 channel relay, anaerobic fermenter = coupled

"""
# Default Starting dictionary.
stages = [{
    "stage": 1,
    "effluent": 400
},
    {
    "stage": 2,
    "influent": 300
},
    {
    "stage": 3,
    "n2": 100
},
    {
    "stage": 4,
    "still": 1300
},
    {
    "stage": 5,
    "air": 5700
},
    {
    "stage": 6,
    "still": 600
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
    WaitTime = 10
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

        time.sleep(WaitTime)
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

        if "n2" in step.keys():
            n2(step["n2"])

        elif "air" in step.keys():
            air(step["air"])

        elif "fermN2" in step.keys():
            fermN2(step["fermN2"])

        elif "influent" in step.keys():
            stepper(step["influent"], "in")

            # turn off
            for pin in range(0, 1):
                # xpin = Stepper1Pins[pin]
                # xpin.off()
                pass

        elif "still" in step.keys():
            still(step["still"])

        elif "effluent" in step.keys():
            stepper(step["effluent"], "out")

            # turn off
            for pin in range(0, 1):
                # xpin = Stepper2Pins[pin]
                # xpin.off()
                pass

        elif "fermenter" in step.keys():
            #stepper(step["fermenter"], None)
            # turn off
            for pin in range(0, 1):
                # xpin = Stepper3Pins[pin]
                # xpin.off()
                pass

        else:
            print("error", print(step))


if __name__ == '__main__':

    while True:
        runCycle()
