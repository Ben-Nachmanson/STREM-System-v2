import board
import busio
from timeit import default_timer as timer
from PyQt5 import QtCore
from gpiozero import OutputDevice
from anyleaf import phSensor, OnBoard

# import Hardware

"""
    Sequential Batch Reactor, 8 channel relay, anaerobic fermenter = coupled

"""
LOOP_DELAY = 60 * 5
i2c = busio.I2C(board.SCL, board.SDA)
phSensor = PhSensor(i2c, LOOP_DELAY)


class Relay(OutputDevice):
    def __init__(self, pin, active_high):
        super(Relay, self).__init__(pin, active_high)


# Default starting stages with MAX = 10 stages
# This is basically the spreadsheet. index = rows(1-10), (stage,stage mode, time) = cols(1,2,3)
# IMPORTANT: IF THERE IS NO Stage just set "stage": NONE , "stage mode" = NONE, "time " = NONE
stages = [{
    "stage": 1,
    "stage mode": "air",
    "time": 20
},
    {
    "stage": 2,
    "stage mode": "n2",
    "time": 15
},
    {
    "stage": 3,
    "stage mode": "still",
    "time": 5
},
    {
    "stage": 4,
    "stage mode": "air",
    "time": 4
},
    {
    "stage": None,
    "stage mode": None,
    "time": None
},
    {
    "stage": None,
    "stage mode": None,
    "time": None
},
    {

    "stage": None,
    "stage mode": None,
    "time": None
}, {

    "stage": None,
    "stage mode": None,
    "time": None
},
    {

    "stage": None,
    "stage mode": None,
    "time": None
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
RELAY_n2 = Relay(6, False)  # n2
RELAY_air = Relay(26, False)  # air
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

# Calculates List Length til None is met


def ListLength():
    i = 0
    for step in stages:
        if(step["stage"] == None):
            break
        i += 1
    return i

# Calculates Total Time in current stages


def TotalTime(startStage):
    sum = 0
    for step in stages:
        try:
            if(int(startStage) <= step["stage"]):
                sum = sum + step["time"]
        except:
            break
            # if None it just goes here.
    return sum

# Checks which stage and turns it on


def TurnOnStage(stageMode):
    if(stageMode == "n2"):
        RELAY_n2.on()
        print("n2 on")
        pass

    elif(stageMode == "air"):
        RELAY_air.on()
        print("air on")
        pass
    elif(stageMode == "fermN2"):
        # RELAY_14.on()
        print("fermN2 on")
        pass
    elif(stageMode == "influent"):
        # in
        # StepPins = Stepper1Pins

        print("influent on")

        pass
    elif(stageMode == "effluent"):
        # out
        # StepPins = Stepper2Pins
        print("effluent on")

        pass
    elif(stageMode == "fermenter"):
       # none
       # StepPins = Stepper3Pins
        print("fermenter on")

        pass
    elif(stageMode == "still"):
        # Do nothing --- Wait
        print("still on")

        pass
    else:
        # Error
        pass

# Checks which stage and turns it off


def TurnOffStage(stageMode):
    if(stageMode == "n2"):
        RELAY_n2.on()
        print("n2 off")
        pass

    elif(stageMode == "air"):
        RELAY_air.on()
        print("air off")
        pass
    elif(stageMode == "fermN2"):
        # RELAY_14.off()
        print("fermN2 off")
        pass
    elif(stageMode == "influent"):
        # turn off
        for pin in range(0, 1):
            # xpin = Stepper1Pins[pin]
            # xpin.off()
            pass

        print("influent off")

        pass
    elif(stageMode == "effluent"):
        # turn off
        for pin in range(0, 1):
            # xpin = Stepper2Pins[pin]
            # xpin.off()
            pass
        print("effluent off")

        pass
    elif(stageMode == "fermenter"):
        # turn off
        for pin in range(0, 1):
            # xpin = Stepper3Pins[pin]
            # xpin.off()
            pass
        print("fermenter off")

        pass
    elif(stageMode == "still"):
        # Do nothing --- Wait
        print("still off")

        pass
    else:
        # Error
        pass


def ReadPh():
    ph = phSensor.read(OnBoard())
    return ph
