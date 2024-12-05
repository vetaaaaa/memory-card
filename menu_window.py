from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton

menu_window = QWidget()
menu_window.setWindowTitle("menu")

label1 = QLabel("Введіть запитання: ")
label2 = QLabel("Введіть вірну відповідь: ")
label3 = QLabel("Введіть 1 хибну відповідь: ")
label4 = QLabel("Введіть 2 хибну відповідь: ")
label5 = QLabel("Введіть 3 хибну відповідь: ")

line_v1 = QVBoxLayout()
line_v1.addWidget(label1)
line_v1.addWidget(label2)
line_v1.addWidget(label3)
line_v1.addWidget(label4)
line_v1.addWidget(label5)

input1 = QLineEdit()
input2 = QLineEdit()
input3 = QLineEdit()
input4 = QLineEdit()
input5 = QLineEdit()

line_v2 = QVBoxLayout()
line_v2.addWidget(input1)
line_v2.addWidget(input2)
line_v2.addWidget(input3)
line_v2.addWidget(input4)
line_v2.addWidget(input5)

line_h1 = QHBoxLayout()
line_h1.addLayout(line_v1)
line_h1.addLayout(line_v2)

add_question_button = QPushButton("Додати запитання")
clear_button = QPushButton("Очистити")

line_h2 = QHBoxLayout()
line_h2.addWidget(add_question_button)
line_h2.addWidget(clear_button)

statistics = QLabel()
back_button = QPushButton("Назад")

menu_layout = QVBoxLayout()
menu_layout.addLayout(line_h1)
menu_layout.addLayout(line_h2)
menu_layout.addWidget(statistics)
menu_layout.addWidget(back_button)
menu_window.setLayout(menu_layout)
menu_window.hide()
