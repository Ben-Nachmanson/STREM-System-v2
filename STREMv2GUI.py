# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'STREMv2GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import main
import sys

# Code for UI objects


class Ui_MainWindow(object):
    # UI naming and positioning
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
        # self.tableWidget.setItem(1, 2, QtWidgets.QTableWidgetItem(str(40)))
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
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setObjectName("reset")
        self.gridLayout.addWidget(self.reset, 6, 2, 1, 1)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.phLabel.setText(_translate("MainWindow", "pH "))
        self.timerLabel.setText(
            _translate("MainWindow", "Timer"))
        self.orpTextBrowser.setPlaceholderText(
            _translate("MainWindow", "0.00"))
        self.orpTextBrowser.setPlainText("0.000")
        self.TimeTextBrowser.setPlaceholderText(
            _translate("MainWindow", "0:00"))
        self.StartStageLabel.setText(_translate("MainWindow", "Start Stage"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Stage"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Stage Mode"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Duration (s)"))
        self.orpLabel.setText(_translate("MainWindow", "ORP"))
        self.phTextBrowser.setPlaceholderText(_translate("MainWindow", "0.00"))
        self.phTextBrowser.setPlainText("0.000")
        self.startStageTextEdit.setPlaceholderText(
            _translate("MainWindow", "1"))
        self.startButton.setText(_translate("MainWindow", "Start"))

        # -------------- Start Button Click Event-------------------
        self.startButton.clicked.connect(self.Start)
        # ----------------------------------------------------------

        self.PauseButton.setText(_translate("MainWindow", "Pause"))

        # -------------- Pause Button Click Event-------------------
        self.PauseButton.clicked.connect(self.Pause)
        # ----------------------------------------------------------

        self.reset.setText(_translate("MainWindow", "Reset"))

        # -------------- Reset Button Click Event-------------------
        self.reset.clicked.connect(self.Reset)
        # ----------------------------------------------------------

        # https://www.geeksforgeeks.org/pyqt5-digital-stopwatch/
        # -------------- Initialize Timer --------------------------
        timer = QtCore.QTimer(MainWindow)
        timer.setTimerType(QtCore.Qt.PreciseTimer)

        timer.timeout.connect(self.ShowTime)
        timer.timeout.connect(self.StageTracker)
        # sets default total time starting at stage 1
        self.count = main.TotalTime(1)
        self.startStageTextEdit.setPlainText(str(1))

        self.flag = False
        timer.start(1000)

        # --------------- Initialize sheet -------------------------------
        self.LoadList()
        self.tableWidget.cellChanged.connect(self.UpdateCell)
        # Keeps track of the current stage.
        self.currentStage = int(self.startStageTextEdit.toPlainText())

        # ----------------------------------------------------------

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.saveAction.setText(_translate("MainWindow", "Save"))
        self.loadAction.setText(_translate("MainWindow", "Load"))
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

    def Start(self):
        # making flag to true
        self.flag = True

    def Pause(self):
        # making flag to False
        self.flag = False

    def Reset(self):
        # making flag to false
        self.flag = False

        # resetting the count
        self.count = main.TotalTime(self.startStageTextEdit.toPlainText())
        self.currentStage = int(self.startStageTextEdit.toPlainText())

        # setting text to label
        self.TimeTextBrowser.setText(str(self.count))
    # *******Sheet Functions***********
    # Loads stages into the gui sheet

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

    def UpdateCell(self):
        col = self.tableWidget.currentColumn()
        row = self.tableWidget.currentRow()

        if col == 0:
            itemType = "stage"
        elif col == 1:
            itemType = "stage mode"
        elif col == 2:
            itemType = "time"

        if(itemType == "stage mode"):

            main.stages[row][itemType] = self.tableWidget.item(row, col).text()
        else:
            try:

                main.stages[row][itemType] = int(
                    self.tableWidget.item(row, col).text())
            except:
                main.stages[row][itemType] = None

        print("entered")
    # *******Stage Functions*************
    # Keeps track of the current stage and triggering next stage.

    def StageTracker(self):
        # index --- start index
        i = int(self.startStageTextEdit.toPlainText()) - 1
        # countDown runtime
        runTime = main.TotalTime(
            self.startStageTextEdit.toPlainText()) - self.count
        # sum of current stages
        stageSum = 0
        # check to see if time is running.
        if self.flag:
            while runTime != stageSum:
                if main.stages[i]["time"] is None:
                    break
                stageSum = main.stages[i]["time"] + stageSum
                i += 1
            if main.TotalTime(self.startStageTextEdit.toPlainText()) == stageSum:
                self.flag = False
            else:
                self.currentStage = i + 1
        print(self.currentStage)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
