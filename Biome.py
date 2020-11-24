from PyQt5 import QtWidgets


class Biome:
    def __init__(self, layout, colors, colors_iterator):
        self.colors = colors
        self.colors_iterator = colors_iterator
        self.layout = layout
        self.initUI()

    def initUI(self):

        #  widgets logic and connections
        self.sliders = []
        self.checkers = []
        self.widgets = (self.layout.itemAt(i).widget() for i in range(self.layout.count()))
        # Loop through widgets in grid
        for widget in self.widgets:
            if isinstance(widget, QtWidgets.QSlider):
                self.sliders.append(widget)
                # Connect slider to def
                widget.valueChanged.connect(self.set_color_level)
            if isinstance(widget, QtWidgets.QCheckBox):
                # Connect checkBox to def
                self.checkers.append(widget)
                widget.stateChanged.connect(self.set_sliders_enabled)

        # lists of sliders and checkBoxes
        self.sliders = sorted(self.sliders, key=lambda x: x.objectName())
        self.checkers = sorted(self.checkers, key=lambda x: x.objectName())

        # Sliders like in qt app
        self.sliders_top_downlike = sorted(self.sliders, key=lambda x: x.value())

    # is slider enabled?
    def set_sliders_enabled(self):
        for slider, checker, color in zip(self.sliders, self.checkers, self.colors_iterator):
            color[1] = checker.isChecked()
            slider.setEnabled(checker.isChecked())
            self.colors[-1][1] = self.colors[-2][1]

    # set color maximum level, set slider minimum value
    def set_color_level(self):
        # set color maximum level
        for color, slider in zip(self.colors_iterator, self.sliders):
            color[0] = slider.value()
        # set correct sliders minimum values
        for i in range(len(self.sliders_top_downlike) - 1):
            if self.sliders_top_downlike[i].isEnabled():
                self.sliders_top_downlike[i + 1].setMinimum(self.sliders_top_downlike[i].value() + 1)

    # return list of colors
    def get_colors(self):
        colors = [i for i in self.colors if i[1]]
        return colors


