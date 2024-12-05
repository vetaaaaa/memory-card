from PyQt5.QtWidgets import QPushButton, QSpinBox, QLabel, QHBoxLayout, QGroupBox, QButtonGroup, QRadioButton, \
    QVBoxLayout, QApplication
from PyQt5.QtCore import Qt

app = QApplication([])
button_menu = QPushButton("Меню")
button_rest = QPushButton("Відпочити")
sp_rest = QSpinBox()
sp_rest.setValue(30)
rest_text = QLabel("Хвилин")

line1 = QHBoxLayout()
line1.addWidget(button_menu)
line1.addStretch(1)
line1.addWidget(button_rest)
line1.addWidget(sp_rest)
line1.addWidget(rest_text)

label_question = QLabel("лолилол")

group_box = QGroupBox("Варіанти відповідей")
rb_group = QButtonGroup()
button_ans1 = QRadioButton("ура")
button_ans2 = QRadioButton("ура")
button_ans3 = QRadioButton("ура")
button_ans4 = QRadioButton("ура")

rb_group.addButton(button_ans1)
rb_group.addButton(button_ans2)
rb_group.addButton(button_ans3)
rb_group.addButton(button_ans4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(button_ans1)
layout_ans2.addWidget(button_ans2)
layout_ans3.addWidget(button_ans3)
layout_ans3.addWidget(button_ans4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
group_box.setLayout(layout_ans1)

ans_group_box = QGroupBox("Перевірка результатів")
lb_resul = QLabel("")
lb_correct = QLabel("")

layout_result = QVBoxLayout()
layout_result.addWidget(lb_resul, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(lb_correct, alignment = Qt.AlignCenter, stretch = 2)
ans_group_box.setLayout(layout_result)
ans_group_box.hide()

button_next = QPushButton("Відповісти")
layout_menu = QVBoxLayout()
layout_menu.addLayout(line1, stretch = 1)
layout_menu.addWidget(label_question, stretch = 2, alignment = Qt.AlignCenter)
layout_menu.addWidget(group_box, stretch = 8)
layout_menu.addWidget(ans_group_box, stretch = 8)
layout_menu.addWidget(button_next, stretch = 1)

def show_result():
    group_box.hide()
    ans_group_box.show()
    button_next.setText("Наступне питання")
def show_question():
    group_box.show()
    ans_group_box.hide()
    button_next.setText("Відповісти")
    rb_group.setExclusive(False)
    button_ans1.setChecked(False)
    button_ans2.setChecked(False)
    button_ans3.setChecked(False)
    button_ans4.setChecked(False)
    rb_group.setExclusive(True)
