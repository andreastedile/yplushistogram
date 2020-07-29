from PyQt5.QtWidgets import QGroupBox, QLabel, QVBoxLayout


class Stats(QGroupBox):
    def __init__(self):
        super().__init__('Stats')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self._facesCount = QLabel('Faces count:')
        self.layout.addWidget(self._facesCount)

        self._surfaceArea = QLabel('Surface area:')
        self.layout.addWidget(self._surfaceArea)

        self._avgYplus = QLabel('Average yPlus:')
        self.layout.addWidget(self._avgYplus)

    @property
    def facesCount(self):
        return self._facesCount.text()

    @facesCount.setter
    def facesCount(self, val: int):
        self._facesCount.setText('Faces count: ' + str(val))

    @property
    def surfaceArea(self):
        return self._surfaceArea.text()

    @surfaceArea.setter
    def surfaceArea(self, val: float):
        self._surfaceArea.setText('Surface area: ' + str(val))

    @property
    def avgYplus(self):
        return self._avgYplus.text()

    @avgYplus.setter
    def avgYplus(self, val: float):
        self._avgYplus.setText('Average yPlus: ' + str(val))
