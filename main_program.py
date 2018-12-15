import sys
from pydub import AudioSegment
from pydub.playback import play
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.QtCore import QTimer, QEventLoop


class MyFirstProgram(QWidget):
    def __init__(self):
        super().__init__()

        self.start = 0

        self.end = 0

        self.on_the_edge = False

        self.setGeometry(300, 300, 900, 900)  # создаю поле программы
        self.setWindowTitle('Музыкальный редактор')

        self.btn = QPushButton('Обрезать по краям или то, что внутри', self)  # создается кнопка, с помощью которой
        self.btn.resize(self.btn.sizeHint())  # можно выбрать то, что именно надо вырезать (концы или середину)
        self.btn.move(70, 150)
        self.btn.clicked.connect(self.change)

        self.label = QLabel(self)  # создается строка, которая показывает, что именно вырезается в данный момент
        self.label.setStyleSheet("background-color:rgb(239, 255, 60)")
        self.label.setText("Я обрезаю то, что внутри")
        self.label.move(70, 30)

        self.file = QLabel(self)  # создается строка, в которую будет вписано название файла
        self.file.setText("Путь до файла:")
        self.file.move(40, 60)

        self.file_input = QLineEdit(self)
        self.file_input.move(135, 60)

        self.start_label = QLabel(self)  # вводятся секунды, по которым надо обрезать
        self.start_label.setText("Введите секунду, с которой надо обрезать: ")
        self.start_label.move(70, 90)

        self.end_label = QLabel(self)
        self.end_label.setText("Введите секунду, по которою надо обрезать: ")
        self.end_label.move(70, 120)

        self.start_input = QLineEdit(self)
        self.start_input.move(340, 90)

        self.end_input = QLineEdit(self)
        self.end_input.move(340, 120)

        self.music_button = QPushButton('Воспроизвести то, что получилось', self)  # кнопка воспроизведения
        self.music_button.move(320, 150)
        self.music_button.clicked.connect(self.music)

        self.m_start = QLabel(self)  # воспроизведение с определенного момента до определенного
        self.m_start.setText('Воспроизвести с ')
        self.m_start.move(40, 200)

        self.m_input = QLineEdit(self)
        self.m_input.move(145, 200)

        self.m_middle = QLabel(self)
        self.m_middle.setText('секунды по ')
        self.m_middle.move(285, 200)

        self.mus_input = QLineEdit(self)
        self.mus_input.move(365, 200)

        self.m_end = QLabel(self)
        self.m_end.setText('секунду')
        self.m_end.move(505, 200)

        self.play_m = QPushButton('Играть', self)
        self.play_m.move(563, 199)
        self.play_m.clicked.connect(self.music)

        self.wrong_file = QLabel(self)  # строка ошибки связанной с вовпроизведением файла
        self.wrong_file.setStyleSheet("color:rgb(246, 246, 246)")  # делает эту строку невидимой (изменяет цвет)
        self.wrong_file.setText('Файл не найден или не соответствует формату. Повторите ввод')
        self.wrong_file.move(400, 60)

        self.song = 0  # переменная, у которой, если значение 0, то значит, что надо считать название файла
        # иначе не надо

        self.wrong_start = QLabel(self)  # ошибка, сообщающая что проблема с секундами
        self.wrong_start.setStyleSheet("color:rgb(246, 246, 246)")
        self.wrong_start.setText('Введеные Вами данные не соответствуют формату. Повторите ввод')
        self.wrong_start.move(40, 250)

        self.wrong_ind = QLabel(self)  # проблема, сообщающая, что конец находится за песней
        self.wrong_ind.setStyleSheet("color:rgb(246, 246, 246)")
        self.wrong_ind.setText('Вы вышли за границу песни. Проверьте введенные вами данные.')
        self.wrong_ind.move(445, 250)

        self.save_music = QPushButton('Сохранить изменения', self)  # сохранение изменений
        self.save_music.move(500, 290)
        self.save_music.clicked.connect(self.save)

        self.m_middle = QLabel(self)
        self.m_middle.setText('Сохранить песню. Путь до песни с ее названием')
        self.m_middle.move(40, 290)

        self.mus_save = QLineEdit(self)
        self.mus_save.move(340, 290)

        self.change_temp = QPushButton('Изменить темп', self)
        self.change_temp.move(510, 260)
        self.change_temp.clicked.connect(self.temp_change)

        self.change_label = QLabel(self)
        self.change_label.setText('На сколько процентов быстрее надо сделать музыку')
        self.change_label.move(40, 260)

        self.change_Edit = QLineEdit(self)
        self.change_Edit.move(360, 260)

    def wrong_f(self):  # Функция, которая заставляет появляться строчку, в случае, если файл введен неверно
        self.wrong_file.setStyleSheet("color:rgb(0, 0, 0)")  # строчка становится видна
        self.wrong_file.setStyleSheet("background-color:rgb(255, 68, 68)")
        self.wrong_file.setText('Файл не найден или не соответствует формату. Повторите ввод')
        self.wrong_file.move(400, 60)

        loop = QEventLoop()  # создается задержка
        QTimer.singleShot(3000, loop.quit)  # первый параметр - время задержки, указывается в милисек.
        loop.exec()

        self.wrong_file.setStyleSheet("color:rgb(246, 246, 246)")  # строчка перестает быть видна
        self.wrong_file.setText('Файл не найден или не соответствует формату. Повторите ввод')
        self.wrong_file.move(400, 60)

    def wrong_start_or_end(self):  # функция, выводящая ошибку, если что-то не так с секундами
        self.wrong_start.setStyleSheet("color:rgb(0, 0, 0)")  # строчка становится видна
        self.wrong_start.setStyleSheet("background-color:rgb(255, 68, 68)")
        self.wrong_start.setText('Введеные Вами данные не соответствуют формату. Повторите ввод')
        self.wrong_start.move(40, 235)

        loop = QEventLoop()  # создается задержка
        QTimer.singleShot(3000, loop.quit)  # первый параметр - время задержки, указывается в милисек.
        loop.exec()

        self.wrong_start.setStyleSheet("color:rgb(246, 246, 246)")  # строчка перестает быть видна
        self.wrong_start.setText('Введеные Вами данные не соответствуют формату. Повторите ввод')
        self.wrong_start.move(40, 235)

    def wrong_index(self):  # функция, выводящая ошибку, если вышли за границу песни
        self.wrong_ind.setStyleSheet("color:rgb(0, 0, 0)")  # строчка становится видна
        self.wrong_ind.setStyleSheet("background-color:rgb(255, 68, 68)")
        self.wrong_ind.setText('Вы вышли за границу песни. Проверьте введенные вами данные. Повторите ввод')
        self.wrong_ind.move(445, 235)

        loop = QEventLoop()  # создается задержка
        QTimer.singleShot(3000, loop.quit)  # первый параметр - время задержки, указывается в милисек.
        loop.exec()

        self.wrong_ind.setStyleSheet("color:rgb(246, 246, 246)")  # строчка перестает быть видна
        self.wrong_ind.setText('Вы вышли за границу песни. Проверьте введенные вами данные. Повторите ввод')
        self.wrong_ind.move(445, 235)

    def temp_change(self):
        try:
            speed = int(self.change_Edit.text())
            if self.song == 0:
                file_name = self.file_input.text()
                self.song = AudioSegment.from_mp3(file_name)
            self.song = self.song._spawn(self.song.raw_data,
                                                      overrides={"frame_rate": int(self.song.frame_rate * speed)})
        except ValueError:
            self.wrong_start_or_end()
        except TypeError:
            self.wrong_start_or_end()
        except Exception:
            self.wrong_f()

    def save(self):  # функция сохранения
        try:
            file_name = self.mus_save.text()
            if self.song == 0:
                file_name1 = self.file_input.text()
                self.song = AudioSegment.from_mp3(file_name1)
            self.song.export(file_name, format='mp3')
        except Exception:
            self.wrong_f()

    def change(self):  # эта функция меняет то, что я буду удалять.
        self.on_the_edge = True if not self.on_the_edge else False
        if not self.on_the_edge:  # либо я буду удалять то, что снаружи,
            self.label.setText('Я обрезаю то, что внутри')
            self.start_label.setText("Введите секунду, с которой надо обрезать: ")
            self.end_label.setText("Введите секунду, по которою надо обрезать: ")
        else:  # либо то, что внутри
            self.label.setText('Я обрезаю по краям')
            self.start_label.setText("Введите секунду, по которою надо обрезать: ")
            self.end_label.setText("Введите секунду, с которой надо обрезать: ")

    def music(self):  # воспроизведение музыки
        try:
            if self.song == 0:  # если еще не считывали файл с песней
                file_name = self.file_input.text()
                self.song = AudioSegment.from_mp3(file_name)
                self.end = len(self.song)

            song = self.cut(self.song)

            while True:
                try:
                    play(song)
                except KeyboardInterrupt:
                    break
                except Exception:
                    self.wrong_f()
                    break
        except Exception:
            self.wrong_f()

    def cut(self, song):  # функция обрезки музыки, в соответствии заданным параметрам
        try:
            if self.sender().text() == 'Играть':
                self.start = int(self.m_input.text()) * 1000
                self.end = int(self.mus_input.text()) * 1000
                if self.start > self.end or self.end > len(song):
                    raise ValueError
                song = song[self.start:self.end]
                return song

            self.start = int(self.start_input.text()) * 1000
            self.end = int(self.end_input.text()) * 1000

            if self.on_the_edge:
                if self.start > self.end or self.end > len(song):
                    raise ValueError
                self.song = song[self.start:self.end]
            else:
                self.song = song[:self.start] + song[self.end:]
            return self.song
        except ValueError:
            self.wrong_start_or_end()
        except TypeError:
            self.wrong_start_or_end()
        except IndexError:
            self.wrong_index()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyFirstProgram()
    ex.show()
    sys.exit(app.exec())
