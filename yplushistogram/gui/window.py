from PyQt5.QtWidgets import QMainWindow, QToolBar, QWidget, QAction, QFileDialog, QMessageBox
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

import csv

from yplushistogram.data import Face, FaceList
from yplushistogram.gui.poi import POI
from yplushistogram.gui.stats import Stats
from yplushistogram.gui.chart import Chart


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('yPlus Histogram')
        self.setFixedSize(QSize(1000, 800))

        self.faceData = FaceList()

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        file = QAction(QIcon.fromTheme('document-open'), 'Open file', toolbar)
        file.triggered.connect(self.readCsv)
        toolbar.addAction(file)

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.vbox = QVBoxLayout()
        self.centralWidget.setLayout(self.vbox)

        self.topLayout = QHBoxLayout()
        self.vbox.addLayout(self.topLayout)

        self.poi = POI()
        self.topLayout.addWidget(self.poi)

        self.stats = Stats()
        self.topLayout.addWidget(self.stats)

        self.chart = Chart(len(self.poi.pois))
        self.vbox.addWidget(self.chart)
        self.chart.setBarRanges(self.poi.pois)

        self.poi.poiChanged.connect(self.updateChart)

    def readCsv(self):
        csvPath = QFileDialog.getOpenFileName(self, 'Open CSV file', '.', 'CSV(*.csv)')
        if not csvPath or not csvPath[0]:
            return
        faceList = FaceList()
        with open(csvPath[0]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    face = Face(float(row['yPlus']), float(row['Area']))
                    faceList.append(face)
                except KeyError:
                    box = QMessageBox(self)
                    box.setAttribute(Qt.WA_DeleteOnClose)
                    box.setWindowTitle('Invalid CSV file')
                    box.setText('The selected CSV file is not valid. Check if columns "yPlus" and "Area" exist.')
                    box.show()
                    return
                except ValueError:
                    box = QMessageBox(self)
                    box.setAttribute(Qt.WA_DeleteOnClose)
                    box.setWindowTitle('Invalid CSV file')
                    box.setText('The selected CSV file is not valid. All columns must only contain numbers.')
                    box.setDetailedText(' '.join(row[key] for key in row))
                    box.show()
                    return

        self.faceData.clear()
        for face in faceList:
            self.faceData.append(face)

        self.updateStats()
        self.updateChart()

    def updateStats(self):
        self.stats.facesCount = len(self.faceData)
        self.stats.surfaceArea = round(self.faceData.surfaceArea(), 2)
        self.stats.avgYplus = round(self.faceData.avgYplus(), 3)

    def updateChart(self):
        pois = self.poi.pois
        self.chart.setBarRanges(pois)

        surfaceArea = self.faceData.surfaceArea()
        if surfaceArea == 0.:
            # Otherwise we divide by zero
            return

        percentages = []
        for i in range(len(pois)):
            if i == 0:
                percentage = self.faceData.bandSurfaceArea(0., pois[0]) * 100 / surfaceArea
            elif i == len(pois) - 1:
                percentage = self.faceData.bandSurfaceArea(pois[len(pois) - 1], float('inf')) * 100 / surfaceArea
            else:
                percentage = self.faceData.bandSurfaceArea(pois[i], pois[i + 1]) * 100 / surfaceArea
            percentages.append(round(percentage, 2))

        self.chart.setBarValues(percentages)
