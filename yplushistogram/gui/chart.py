from typing import List

from PyQt5.QtChart import QChartView, QChart, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


class Chart(QChartView):
    def __init__(self, barCount: int):
        super().__init__()

        self.chart = QChart()
        self.setChart(self.chart)
        self.setRenderHint(QPainter.Antialiasing)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setBackgroundVisible(True)
        self.chart.legend().setVisible(False)

        self.series = QBarSeries()
        self.chart.addSeries(self.series)

        self.barValues = QBarSet('')
        self.series.append(self.barValues)
        for i in range(barCount):
            self.barValues << 0.

        self.xAxis = QBarCategoryAxis()
        self.chart.addAxis(self.xAxis, Qt.AlignBottom)
        self.series.attachAxis(self.xAxis)
        self.xAxis.setTitleText('yPlus ranges')

        self.yAxis = QValueAxis()
        self.chart.addAxis(self.yAxis, Qt.AlignLeft)
        self.series.attachAxis(self.yAxis)
        self.yAxis.setTitleText('% of surface area')
        self.yAxis.setRange(0, 100)

    def setBarRanges(self, pois: List[float]):
        for i in range(len(pois)):
            if i == 0:
                tag = 'lt ' + str(pois[0])
            elif i == len(pois) - 1:
                tag = 'gt ' + str(pois[-1])
            else:
                tag = str(pois[i]) + ' - ' + str(pois[i + 1])

            if not self.xAxis.count():
                self.xAxis.append(tag)
            else:
                self.xAxis.replace(self.xAxis.at(i), tag)

    def setBarValues(self, values: List[float]):
        assert len(values) == self.barValues.count()

        for i in range(len(values)):
            if not self.barValues.count():
                self.barValues.insert(i, 0.)
            else:
                self.barValues.replace(i, values[i])
