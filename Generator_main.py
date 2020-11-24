from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from UI import Ui_MainWindow
from PIL.ImageQt import ImageQt
from perlin_noise_image_creator import generate_perlin_noise, add_color
import sys
from Forest import Forest
from Desert import Desert
from Frost import Frost
from FAQ import FAQ


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_UI()

    # Setting elements, connections and logic
    def init_UI(self):

        self.FAQ.clicked.connect(self.show_faq)

        self.Generate_button.clicked.connect(self.generate_image_main_logic)

        self.Save_button.setEnabled(False)
        self.Save_button.clicked.connect(self.save_image)

        # base_settings_update connections
        self.base_settings = {'size': 200, 'zoom': 50}
        self.Size_ComboBox.valueChanged.connect(self.base_settings_update)
        self.Zoom_ComboBox.valueChanged.connect(self.base_settings_update)
        # Biomes
        self.Forest = Forest(self.ForestLayout)
        self.Desert = Desert(self.DesertLayout)
        self.Frost = Frost(self.FrostLayout)

    def generate_image_main_logic(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        # Generate default noise
        if self.Generation_ComboBox.currentText() == 'Default':
            print('Generated default map')
            self.image = generate_perlin_noise(self.base_settings)
        # Generate forest map
        elif self.Generation_ComboBox.currentText() == 'Forest':
            print('Generated forest map')
            self.image = add_color(generate_perlin_noise(self.base_settings), self.Forest.get_colors())
        # Generate desert map
        elif self.Generation_ComboBox.currentText() == 'Desert':
            print('Generated desert map')
            self.image = add_color(generate_perlin_noise(self.base_settings), self.Desert.get_colors())
        # Generate frost map
        elif self.Generation_ComboBox.currentText() == 'Frost':
            print('Generated frost map')
            self.image = add_color(generate_perlin_noise(self.base_settings), self.Frost.get_colors())

        # Pixmap set
        tmp_img = ImageQt(self.image)
        pixmap = QPixmap.fromImage(tmp_img)
        self.Result.setPixmap(pixmap)
        self.Save_button.setEnabled(True)

        QApplication.restoreOverrideCursor()

    # Save image
    def save_image(self):
        file_name = QFileDialog.getSaveFileName(self, 'Save', '', '*.png')[0]
        if file_name:
            save_file = self.image
            save_file.save(file_name)

    # Updating base_settings dict
    def base_settings_update(self):
        self.base_settings['size'] = self.Size_ComboBox.value()
        self.base_settings['zoom'] = self.Zoom_ComboBox.value()
        print(self.base_settings)

    def show_faq(self):
        self.faq = FAQ()
        self.faq.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
