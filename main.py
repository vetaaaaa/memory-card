from random import shuffle, choice
from main_window import *
from question_card import QuestionCard
from menu_window import *
global cur_q

text_wrong = "Неправильно"
text_correct = "Правильно"

questions = [
    QuestionCard("Яблуко", "Apple", "Application"
             , "Building","Orange"),
    QuestionCard("Апельсин", "Orange", "Application"
             , "Building","Apple"),
    QuestionCard("Авокадо", "Avocado", "Avocadododo"
             , "Building","Apple")
]

form_question = ""
form_right = ""
form_wrong1 = ""
form_wrong2 = ""
form_wrong3 = ""

button_list = [button_ans1, button_ans2, button_ans3, button_ans4]
shuffle(button_list)
right_answer = button_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = button_list[1], button_list[2], button_list[3]

window = QWidget()
window.resize(600, 500)
window.setWindowTitle("Memory card")
window.setLayout(layout_menu)

def answer_button_click():
    if button_next.text() != "Наступне питання":
        check_result()
    else:
        new_question()
        show_data()
        show_question()

def new_question():
    global cur_q
    global form_question, form_right, form_wrong1, form_wrong2, form_wrong3
    cur_q = choice(questions)
    form_question = cur_q.question
    form_right = cur_q.right_ans
    form_wrong1 = cur_q.wrong_ans1
    form_wrong2 = cur_q.wrong_ans2
    form_wrong3 = cur_q.wrong_ans3

def show_data():
    label_question.setText(form_question)
    lb_correct.setText(form_right)
    right_answer.setText(form_right)
    wrong_answer1.setText(form_wrong1)
    wrong_answer2.setText(form_wrong2)
    wrong_answer3.setText(form_wrong3)

def check_result():
    correct = right_answer.isChecked()
    if correct:
        lb_resul.setText(text_correct)
        show_result()
        print(1)
        cur_q.got_right()
    else:
        incorrect = (wrong_answer1.isChecked() or
                     wrong_answer2.isChecked() or
                     wrong_answer3.isChecked() )
        if incorrect:
            lb_resul.setText(text_wrong)
            show_result()
            print(2)
            cur_q.got_wrong()

def open_menu():
    if QuestionCard.attempts == 0:
        count = 0
    else:
        count = (QuestionCard.correct / QuestionCard.attempts) * 100

    result = (f'Разів відповіли: {QuestionCard.attempts}\n' \
           f'Вірних відповідей: {QuestionCard.correct}\n' \
           f'Успішність: {round(count, 2)}%')
    statistics.setText(result)
    window.hide()
    menu_window.show()

def open_main():
    menu_window.hide()
    window.show()

def add_question():
    new_q = QuestionCard(input1.text(), input2.text(), input3.text(), input4.text(), input5.text())
    questions.append(new_q)

def clear():
    input1.clear()
    input2.clear()
    input3.clear()
    input4.clear()
    input5.clear()

add_question_button.clicked.connect(add_question)
clear_button.clicked.connect(clear)
back_button.clicked.connect(open_main)
button_menu.clicked.connect(open_menu)

button_next.clicked.connect(answer_button_click)
new_question()

window.setStyleSheet("""
    QWidget {
        background-color: #c8beb9;
        font-size: 16px;
    }
    
    QPushButton {
        background-color: #a81817;
        color: #f0f4f7;
        padding: 5px 10px;
        border-radius: 5px;
        border: 1px solid grey;
    }
    
    QPushButton:hover {
        background-color: #781111;
        color: #f0f4f7;
    }
    
    QGroupBox {
        background-color: #598251;
        color: #f0f4f7;
        border: 2px solid #f0f4f7; 
        border-radius: 5px;
        padding: 10px;
    }
    
    QRadioButton {
        background-color: #598251;
        color: #f0f4f7;
        font-size: 20px;
    }
    
    
""")

window.show()
app.exec_()