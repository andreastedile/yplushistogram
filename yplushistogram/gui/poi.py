from __future__ import annotations

from PyQt5.QtWidgets import QGroupBox, QFormLayout, QAbstractSpinBox, QDoubleSpinBox, QLabel
from PyQt5.QtCore import pyqtSignal


class POI(QGroupBox):
    defaultPois = [0.1, 3., 5., 11., 30., 300.]

    poiChanged = pyqtSignal(list)  # Emits new POIs

    def __init__(self):
        super().__init__('POIs')

        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self._pois = []
        for i in range(len(self.defaultPois)):
            poi = QDoubleSpinBox()
            self.layout.addRow(QLabel('POI ' + str(i)), poi)
            self._pois.append(poi)

            poi.setButtonSymbols(QAbstractSpinBox.NoButtons)

            # Set min values
            if i == 0:
                # First poi
                poi.setRange(0.01, self.defaultPois[i + 1] - 0.1)
            elif i == len(self.defaultPois) - 1:
                # Last poi
                poi.setRange(self.defaultPois[i - 1] + 0.1, float('inf'))
            else:
                # Middle poi
                poi.setRange(self.defaultPois[i - 1] + 0.1, self.defaultPois[i + 1] - 0.1)

            poi.setValue(self.defaultPois[i])

            poi.valueChanged.connect(self.updatePois)

    def updatePois(self):
        for i in range(len(self._pois)):
            if i > 0:
                self._pois[i - 1].setMaximum(self._pois[i].value() - 0.1)
            if i < len(self._pois) - 1:
                self._pois[i + 1].setMinimum(self._pois[i].value() + 0.1)

        self.poiChanged.emit(self.pois)

    @property
    def pois(self):
        values = []
        for poi in self._pois:
            values.append(poi.value())
        return values
