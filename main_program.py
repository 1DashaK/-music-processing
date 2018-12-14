import sys
from pydub import AudioSegment
from pydub.playback import play
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class MyFirstProgram(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.on_the_edge = False

    def initUI(self):
        self.setGeometry(300, 300, 900, 600)
        self.setWindowTitle('Музыкальный редактор')

        self.btn = QPushButton('Обрезать по краям или то, что внутри', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(70, 150)
        self.btn.clicked.connect(self.change)

        self.label = QLabel(self)
        self.label.setText("Я обрезаю то, что внутри")
        self.label.move(70, 30)

        self.file = QLabel(self)
        self.file.setText("Путь до файла:")
        self.file.move(40, 60)

        self.file_input = QLineEdit(self)
        self.file_input.move(135, 60)

        self.start_label = QLabel(self)
        self.start_label.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.start_label.setText("Введите секунду, с которой надо обрезать: ")
        self.start_label.move(70, 90)

        self.end_label = QLabel(self)
        self.end_label.setText("Введите секунду, по которою надо обрезать: ")
        self.end_label.move(70, 120)

        self.start_input = QLineEdit(self)
        self.start_input.move(340, 90)

        self.end_input = QLineEdit(self)
        self.end_input.move(340, 120)

        self.music_button = QPushButton('Воспроизвести то, что получилось', self)
        self.music_button.move(320, 150)
        self.music_button.clicked.connect(self.music)

        self.m_start = QLabel(self)
        self.m_start.setText('Воспроизвести с ')
        self.m_start.move(40, 200)

        self.m_input = QLineEdit(self)
        self.m_input.move(145, 200)

        self.m_middle = QLabel(self)
        self.m_middle.setText('секунд(ы) по ')
        self.m_middle.move(285, 200)

        self.mus_input = QLineEdit(self)
        self.mus_input.move(365, 200)

        self.m_end = QLabel(self)
        self.m_end.setText('секунд(у)')
        self.m_end.move(505, 200)

        self.play_m = QPushButton('Играть', self)
        self.play_m.move(563, 199)
        self.play_m.clicked.connect(self.music)

    def change(self):  # эта функция меняет то, что я буду удалять.
        self.on_the_edge = True if not self.on_the_edge else False
        if not self.on_the_edge:  # либо я буду удалять то, что снаружи,
            self.label.setText('Я обрезаю по краям')
            self.start_label.setText("Введите секунду, с которой надо обрезать: ")
            self.end_label.setText("Введите секунду, по которою надо обрезать: ")
        else:  # либо то, что внутри
            self.label.setText('Я обрезаю то, что внутри')
            self.start_label.setText("Введите секунду, по которою надо обрезать: ")
            self.end_label.setText("Введите секунду, с которой надо обрезать: ")

    def music(self):
        self.song = AudioSegment.from_mp3(self.file_name)
        while True:
            try:
                play(self.song)
            except KeyboardInterrupt:
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyFirstProgram()
    ex.show()
    sys.exit(app.exec())
