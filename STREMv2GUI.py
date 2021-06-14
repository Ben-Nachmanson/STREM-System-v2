# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STREMv2GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
import main
import datetime
import sys
import time

# Code for UI objects


class Ui_MainWindow(object):
    # UI Initialization
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.phLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.phLabel.setFont(font)
        self.phLabel.setObjectName("phLabel")
        self.gridLayout.addWidget(self.phLabel, 1, 2, 1, 1)
        self.timerLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.timerLabel.setFont(font)
        self.timerLabel.setObjectName("timerLabel")
        self.gridLayout.addWidget(self.timerLabel, 3, 2, 1, 4)
        self.orpTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(44)
        self.orpTextBrowser.setFont(font)
        self.orpTextBrowser.setObjectName("orpTextBrowser")
        self.gridLayout.addWidget(self.orpTextBrowser, 2, 4, 1, 2)
        self.TimeTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(44)
        self.TimeTextBrowser.setFont(font)
        self.TimeTextBrowser.setTabletTracking(True)
        self.TimeTextBrowser.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TimeTextBrowser.setMidLineWidth(0)
        self.TimeTextBrowser.setTabChangesFocus(False)
        self.TimeTextBrowser.setObjectName("TimeTextBrowser")
        self.gridLayout.addWidget(self.TimeTextBrowser, 4, 2, 1, 4)
        self.StartStageLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.StartStageLabel.setFont(font)
        self.StartStageLabel.setObjectName("StartStageLabel")
        self.gridLayout.addWidget(self.StartStageLabel, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 8, 1)
        self.orpLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.orpLabel.setFont(font)
        self.orpLabel.setObjectName("orpLabel")
        self.gridLayout.addWidget(self.orpLabel, 2, 2, 1, 1)
        self.phTextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(44)
        self.phTextBrowser.setFont(font)
        self.phTextBrowser.setObjectName("phTextBrowser")
        self.gridLayout.addWidget(self.phTextBrowser, 1, 4, 1, 2)
        self.startStageTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(44)
        self.startStageTextEdit.setFont(font)
        self.startStageTextEdit.setObjectName("startStageTextEdit")
        self.gridLayout.addWidget(self.startStageTextEdit, 0, 4, 1, 2)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.startButton.setPalette(palette)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 5, 2, 1, 1)
        self.PauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.PauseButton.setObjectName("PauseButton")
        self.gridLayout.addWidget(self.PauseButton, 5, 4, 1, 2)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("reset")
        self.gridLayout.addWidget(self.resetButton, 6, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.saveAction = QtWidgets.QAction(MainWindow)
        self.saveAction.setObjectName("saveAction")
        self.loadAction = QtWidgets.QAction(MainWindow)
        self.loadAction.setObjectName("loadAction")
        self.menuFile.addAction(self.saveAction)
        self.menuFile.addAction(self.loadAction)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Setting text and naming
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STREM-System-V2"))
        MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.phLabel.setText(_translate("MainWindow", "pH "))
        self.timerLabel.setText(
            _translate("MainWindow", "Timer"))
        self.orpTextBrowser.setPlaceholderText(
            _translate("MainWindow", "0.00"))
        self.orpTextBrowser.setPlainText("0.000")
        self.StartStageLabel.setText(_translate("MainWindow", "Start Stage"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stage"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Stage Mode"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duration (s)"))
        self.orpLabel.setText(_translate("MainWindow", "ORP"))
        self.phTextBrowser.setPlainText("0.000")
        self.startStageTextEdit.setPlaceholderText(
            _translate("MainWindow", "1"))
        self.startButton.setText(_translate("MainWindow", "Start"))

        # -------------- Start Button Click Event-------------------
        self.startButton.clicked.connect(self.Start)
        # ----------------------------------------------------------
        # -------------- Start Stage Text Edit Event-------------------
        self.startStageTextEdit.textChanged.connect(self.StartStageTextCheck)
        # ----------------------------------------------------------

        self.PauseButton.setText(_translate("MainWindow", "Pause"))

        # -------------- Pause Button Click Event-------------------
        self.PauseButton.clicked.connect(self.Pause)
        self.PauseButton.setEnabled(False)
        # ----------------------------------------------------------

        self.resetButton.setText(_translate("MainWindow", "Reset"))

        # -------------- Reset Button Click Event-------------------
        self.resetButton.clicked.connect(self.ResetButtonClicked)
        # ----------------------------------------------------------

        # https://www.geeksforgeeks.org/pyqt5-digital-stopwatch/
        # -------------- Initialize CountDown Timer ---------------
        timer = QtCore.QTimer(MainWindow)
        timer.setTimerType(QtCore.Qt.PreciseTimer)
        self.count = main.TotalTime(1)
        self.startStageTextEdit.setPlainText(str(1))
        self.flag = False
        timer.start(1000)

        # Countdown Timer Events -- functions constantly get checked when timer is running.
        timer.timeout.connect(self.ShowTime)
        timer.timeout.connect(self.HighlightRow)
        timer.timeout.connect(self.StageTracker)
        timer.timeout.connect(self.CycleReset)

        # -------------- Initialize Interval Timer --------------

        intervalTimer = QtCore.QTimer(MainWindow)
        intervalTimer.setTimerType(QtCore.Qt.PreciseTimer)
        intervalTimer.start(1000)
        self.intervalCount = 0

        # Interval Timer Events.

        intervalTimer.timeout.connect(self.IntervalWriteToFile)
        intervalTimer.timeout.connect(self.PHSetter)
        intervalTimer.timeout.connect(self.OrpSetter)

        # ----------- Initialize Stepper Timer --------------
        stepperTimer = QtCore.QTimer(MainWindow)
        stepperTimer.setTimerType(QtCore.Qt.PreciseTimer)
        stepperTimer.start(1000)
        self.stepperCount = 0
        self.stepperTimerFlag = False
        self.stepCounter = 0

        # Stepper Timer Events
        stepperTimer.timeout.connect(self.StepperCheck)

        # --------------- Initialize sheet -------------------------------
        self.LoadList()
        self.tableWidget.cellChanged.connect(self.UpdateCell)
        # Keeps track of the current stage. -1 for index
        self.currentStage = int(self.startStageTextEdit.toPlainText()) - 1

        # ----------------------------------------------------------

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.saveAction.setText(_translate("MainWindow", "Save"))
        self.loadAction.setText(_translate("MainWindow", "Load"))

        self.loadAction.triggered.connect(self.Load)
        self.saveAction.triggered.connect(self.Save)

    # https://www.geeksforgeeks.org/pyqt5-digital-stopwatch/

    # *******Time Functions***********

    def ShowTime(self):

        # checking if flag is true
        if self.flag:

            # decrementing the counter
            self.count -= 1

        # Converting the self.count --"seconds" into hours, mins and secs.
        min, sec = divmod(self.count, 60)
        hour, min = divmod(min, 60)
        # getting text from count

        text = "%d:%02d:%02d" % (hour, min, sec)

        # showing text
        self.TimeTextBrowser.setText(text)
    # activated when the start button is clicked.

    def Start(self):
        # making flag to true
        self.flag = True
        main.TurnOnStage(
            main.stages[self.currentStage]["stage mode"])
        self.StepperCheckOn()

        self.tableWidget.setEnabled(False)
        self.startButton.setEnabled(False)
        self.PauseButton.setEnabled(True)
        self.startStageTextEdit.setEnabled(False)

    def Pause(self):
        # making flag to False
        self.flag = False
        self.stepperTimerFlag = False

        main.TurnOffStage(main.stages[self.currentStage]["stage mode"])
        self.StepperCheckOff(0)

        self.startButton.setEnabled(True)
        self.PauseButton.setEnabled(False)
    # triggered when timer reaches "00:00:00"

    def CycleReset(self):
        if(self.count == 0):
            self.ResetButtonClicked()
            print("Resetting")
            self.Start()
    # Writes to file every five minutes

    def IntervalWriteToFile(self):
        self.intervalCount += 1

        # 300 seconds - > 5 mins - interval count is just the time
        if(self.intervalCount % 300 == 0):
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            now = datetime.datetime.now()

            currentTime = now.strftime("%H:%M:%S")

            date = str(year)+" / "+str(month)+" / " + \
                str(day) + " - " + currentTime
            file = open("PH and Orp Data.txt", "a")

            print(date + " -> "+" pH: " + self.phTextBrowser.toPlainText() +
                  " ORP: " + self.orpTextBrowser.toPlainText() + "\n")
            file.write(date + " -> "+" pH: " + self.phTextBrowser.toPlainText() +
                       " ORP: " + self.orpTextBrowser.toPlainText() + "\n")
            file.close()

        # print(self.intervalCount)

        # ------Interval Timer------------
    # Resets the timer/count/currentStage and sets all the cells backgrounds to white.
    def ResetButtonClicked(self):
        # making flag to false
        self.flag = False
        self.startButton.setEnabled(True)
        self.PauseButton.setEnabled(False)
        self.tableWidget.setEnabled(True)
        self.startStageTextEdit.setEnabled(True)

        if(self.startStageTextEdit.toPlainText() == ''):
            self.currentStage = 0
            self.startStageTextEdit.setPlainText(str(1))

        if(self.count != main.TotalTime(self.startStageTextEdit.toPlainText())):
            if(self.currentStage < len(main.stages)-1):
                main.TurnOffStage(main.stages[self.currentStage]["stage mode"])
                self.StepperCheckOff(0)
            else:
                main.TurnOffStage(
                    main.stages[self.currentStage - 1]["stage mode"])
                self.StepperCheckOff(1)

        self.stepperCount = 0
        # resetting current stage -1 for index
        if(self.startStageTextEdit.toPlainText() != 'invalid'):

            self.currentStage = int(self.startStageTextEdit.toPlainText()) - 1
            self.startStageTextEdit.setPlainText(str(self.currentStage+1))

        # setting text to label

        # resets all cell color backgrounds in table back to white.
        for row in range(self.tableWidget.rowCount()):
            try:
                self.tableWidget.item(row,
                                      0).setBackground(QtGui.QColor(255, 255, 255))
                self.tableWidget.item(row,
                                      1).setBackground(QtGui.QColor(255, 255, 255))
                self.tableWidget.item(row,
                                      2).setBackground(QtGui.QColor(255, 255, 255))
            except:
                pass

    # *******Spreadsheet Functions***********

    # checks if the value entered for the start stage is "valid"
    def StartStageTextCheck(self):
        if(self.startStageTextEdit.toPlainText().isdigit()):
            # If too small or large of a digit
            if(int(self.startStageTextEdit.toPlainText()) > main.ListLength() or int(self.startStageTextEdit.toPlainText()) <= 0):
                self.startStageTextEdit.setPlainText('invalid')
                self.startButton.setEnabled(False)
                self.resetButton.setEnabled(False)
            else:
                # print("valid")
                self.startButton.setEnabled(True)
                self.resetButton.setEnabled(True)
                self.count = main.TotalTime(
                    self.startStageTextEdit.toPlainText())
                self.currentStage = int(
                    self.startStageTextEdit.toPlainText())-1

        elif(self.startStageTextEdit.toPlainText() == ''):
            self.startButton.setEnabled(True)
            self.resetButton.setEnabled(True)

        elif (self.startStageTextEdit.toPlainText() != 'invalid'):
            self.startStageTextEdit.setPlainText('invalid')
            self.startButton.setEnabled(False)
            self.resetButton.setEnabled(False)

        else:
            # print("null")
            pass

    # Loads the dict into the sheet.
    def LoadList(self):
        i = 0
        for item in main.stages:
            if item["stage"] is not None:
                self.tableWidget.setItem(
                    i, 0, QtWidgets.QTableWidgetItem(str(item["stage"])))
                self.tableWidget.setItem(
                    i, 1, QtWidgets.QTableWidgetItem(str(item["stage mode"])))
                self.tableWidget.setItem(
                    i, 2, QtWidgets.QTableWidgetItem(str(item["time"])))
            i += 1

        self.ResetButtonClicked()

    def CheckCells(self):
        for row in range(self.tableWidget.rowCount()):
            try:
                if(self.tableWidget.item(row, 0).text() == "#Name?" or self.tableWidget.item(row, 1).text() == "#Name?" or self.tableWidget.item(row, 2).text() == "#Name?"):
                    self.startButton.setEnabled(False)
                    self.resetButton.setEnabled(False)
                    self.PauseButton.setEnabled(False)
                    self.startStageTextEdit.setEnabled(False)
                    break
                else:
                    self.startButton.setEnabled(True)
                    self.resetButton.setEnabled(True)
                    self.startStageTextEdit.setEnabled(True)
            except:
                pass

    # Empties the sheet of values.

    def ClearSheet(self):
        i = 0
        while(i != self.tableWidget.rowCount()):
            self.tableWidget.setItem(
                i, 0, QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(
                i, 1, QtWidgets.QTableWidgetItem(""))
            self.tableWidget.setItem(
                i, 2, QtWidgets.QTableWidgetItem(""))
            i += 1

    # Writes the the dict when the cells on sheet are changed - along with deactivating buttons.
    def UpdateCell(self):
        col = self.tableWidget.currentColumn()
        row = self.tableWidget.currentRow()
        itemType = None

        if col == 0:
            itemType = "stage"
        elif col == 1:
            itemType = "stage mode"
        elif col == 2:
            itemType = "time"

        if(self.tableWidget.item(row, col)is None):
            pass
        elif(self.tableWidget.item(row, col).text() == ''):
            main.stages[row][itemType] = None
        else:

            if(itemType == "stage mode"):
                if(self.tableWidget.item(row, col).text() in main.stageModes):
                    main.stages[row][itemType] = self.tableWidget.item(
                        row, col).text()
                else:
                    self.tableWidget.item(row, col).setText("#Name?")
            else:
                if(self.tableWidget.item(row, col).text().isdigit()):
                    main.stages[row][itemType] = int(
                        self.tableWidget.item(row, col).text())
                else:
                    self.tableWidget.item(row, col).setText("#Name?")
        self.CheckCells()

    # *******Stage Functions*************

    # Will highlight the current stage to yellow when clock is running
    def HighlightRow(self):
        if self.flag:
            try:
                if(main.stages[self.currentStage]["stage"] is not None or main.stages[self.currentStage]["stage mode"] is not None or main.stages[self.currentStage]["time"]):
                    self.tableWidget.item(self.currentStage,
                                          0).setBackground(QtGui.QColor(255, 255, 0))
                    self.tableWidget.item(self.currentStage,
                                          1).setBackground(QtGui.QColor(255, 255, 0))

                    self.tableWidget.item(self.currentStage,
                                          2).setBackground(QtGui.QColor(255, 255, 0))

            except:
                print("nothing to do")

    # main logic running gui - calculates running time if clock is running
    def StageTracker(self):

        # countDown runtime
        runTime = main.TotalTime(
            self.startStageTextEdit.toPlainText()) - self.count

        # total Timer time
        fullCountdownTime = main.TotalTime(
            self.startStageTextEdit.toPlainText())
        if self.flag:

            # sum of current stages
            stageSum = self.GetStagesSum()

            # Checks to see if it is the last stage
            if fullCountdownTime == stageSum and stageSum == runTime:
                main.TurnOffStage(main.stages[self.currentStage]["stage mode"])
                # Checks if the stepper is running
                self.StepperCheckOff(0)
                self.currentStage += 1
                if(self.currentStage < len(main.stages)-1):
                    main.TurnOnStage(
                        main.stages[self.currentStage]["stage mode"])
                    self.StepperCheckOn()
                    # highlights last row
                    self.HighlightRow()

                # sets timer flag to false
                self.flag = False

            # checks if the stage has gone full runtime
            elif runTime == stageSum:
                main.TurnOffStage(main.stages[self.currentStage]["stage mode"])
                self.StepperCheckOff(0)

                self.currentStage += 1
                main.TurnOnStage(
                    main.stages[self.currentStage]["stage mode"])
                self.StepperCheckOn()

    # returns the sum of stages that have been ran
    def GetStagesSum(self):
        start = int(self.startStageTextEdit.toPlainText())-1
        end = self.currentStage + 1
        sum = 0
        for x in range(start, end):
            try:
                sum = main.stages[x]["time"] + sum
            except:
                print("Empty")
        return sum

    # *******Stepper Functions*************

    # Stepper interval logic
    def StepperCheck(self):

        stepCount = len(main.Seq)
        StepDir = 1  # Set to 1  for clockwise, -1  for anti-clockwise
        waitTime = 10  # Stepper time check interval
        # print("StepperCount" + str(self.stepperCount))
        if self.stepperTimerFlag:
            self.stepperCount += 1

            if(self.stepperCount % waitTime == 0):
                for pin in range(0, 1):
                    # xpin = StepPins[pin]
                    pass
                    if main.Seq[self.stepCounter][pin] != 0:
                        # xpin.on()
                        pass
                    else:
                        # xpin.off()
                        pass
                self.stepCounter += StepDir  # Plus 1 or Minus 1
                print("Next Line:", self.stepCounter)

                if (self.stepCounter >= stepCount):
                    self.stepCounter = 0
                if (self.stepCounter < 0):
                    self.stepCounter = stepCount+StepDir
    # checks if the current Stage requires the stepper to be turned off

    def StepperCheckOff(self, index):
        if(main.stages[self.currentStage-index]["stage mode"] == "effluent" or main.stages[self.currentStage-index]["stage mode"] == "influent" or main.stages[self.currentStage-index]["stage mode"] == "fermenter"):
            self.stepperTimerFlag = False

    # checks if the currentStage requires the stepper to be activated.
    def StepperCheckOn(self):
        if(main.stages[self.currentStage]["stage mode"] == "effluent" or main.stages[self.currentStage]["stage mode"] == "influent" or main.stages[self.currentStage]["stage mode"] == "fermenter"):
            self.stepperTimerFlag = True
            self.stepperCount = 0

    # *******Miscellaneous Functions*************

    # updates ph value constantly
    def PHSetter(self):
        # put real pH reading here later
        # self.phTextBrowser.setPlainText(str(main.ReadPh()).ljust(5)[:5])
        self.phTextBrowser.setPlainText(str("0.00"))

    # Updates Orp value constantly

    def OrpSetter(self):
        # put real Orp reading here later.
        # self.orpTextBrowser.setPlainText(str(main.ReadOrp()).ljust(5)[:5])
        self.orpTextBrowser.setPlainText(str("0.00"))

    # Save
    def Save(self):
        print("save pressed")
        self.SaveDialogBox()

    # Loads a file and updates the startStage
    def Load(self):
        print("loadPressed")
        try:
            self.OpenDialogBox()
            self.ClearSheet()
            self.LoadList()
            # self.currentStage = 0
            self.startStageTextEdit.setPlainText(str(1))
            self.count = main.TotalTime(1)

        except:
            print("file has been tampered with or is in wrong format")

    # opens a file and loads it into stages
    def OpenDialogBox(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            None, "Loading...", "", "Text files(*.txt)")
        path = fileName[0]
        fileList = []
        if(path != ''):
            with open(path, "r") as file:
                fileList = file.readlines()
        # load it back into Stages
        index = 0
        itemType = 0

        for item in fileList:
            item = item.strip('\n')
            if (itemType % 3 == 0):
                if(item != 'None'):
                    main.stages[index]["stage"] = int(item)
                else:
                    main.stages[index]["stage"] = None
            elif(itemType % 3 == 1):
                if(item != 'None'):
                    main.stages[index]["stage mode"] = item
                else:
                    main.stages[index]["stage mode"] = None
            elif(itemType % 3 == 2):
                if(item != 'None'):
                    main.stages[index]["time"] = int(item)
                else:
                    main.stages[index]["time"] = None
                index += 1
            itemType += 1
    # creates a file and saves the current stages to a .txt file

    def SaveDialogBox(self):
        fileName = QtWidgets.QFileDialog.getSaveFileName(
            None, "Save", "", "Text files(*.txt)")
        path = fileName[0]
        i = 0
        if(path != ''):
            with open(path, "w") as file:
                for step in main.stages:

                    file.write(str(step["stage"]) + "\n")
                    file.write(str(step["stage mode"]) + "\n")
                    file.write(str(step["time"]) + "\n")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Splash Screen********************************
    # splash_pix = QtGui.QPixmap('SplashScreen.png')
    # splash = QtWidgets.QSplashScreen(
    #     splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    # # add fade to splashscreen
    # opaqueness = 0.0
    # step = 0.03
    # splash.setWindowOpacity(opaqueness)
    # splash.show()
    # while opaqueness < 1:
    #     splash.setWindowOpacity(opaqueness)
    #     time.sleep(step)  # Sleep for 3 seconds
    #     opaqueness += (2*step)
    # time.sleep(1.2)
    # splash.close()
    # **********************************************
    # main.Stepper(200, "in")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
