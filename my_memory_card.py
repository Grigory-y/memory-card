#создай приложение для запоминания информации
#подключение модулей
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import randint, shuffle

#создание окна
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(300, 200)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Вопрос 1?', '12', '34', '55', '6'))
question_list.append(Question('Вопрос 2?', '10', '434', '15', '6'))
question_list.append(Question('Вопрос 3?', '232', '94', '59', '7'))   

#создание виджетов
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Вопрос?')
RadioGroupBox = QGroupBox('Варианты ответов:')
AnsGroupBox = QGroupBox('Результат теста')

rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

correctans = QLabel('Правильный ответ')
correct_or_not = QLabel('Правильно/Неправильно')

#расположение по layoutам
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_result = QVBoxLayout()
layout_correct_or_not = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_result.addWidget(correct_or_not, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(correctans, alignment = Qt.AlignHCenter)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox.setLayout(layout_result)
AnsGroupBox.setLayout(layout_correct_or_not)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
layout_line3.addStretch(1) #растяжение виджета
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addStretch(1)
layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 2)
layout_card.addLayout(layout_line3, stretch = 2)
layout_ans3.addStretch(1) #пробел между layoutами
layout_card.setSpacing(5) 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

#создание следующего вопроса
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

#перемешка ответов
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    correctans.setText(q.right_answer)
    show_question()

def show_corecct(res):
    correct_or_not.setText(res)
    show_result()

window.score = 0
window.total = 0
#проверка ответа
def check_answer():
    if answers[0].isChecked():
        show_corecct('Правильно!')
        window.score += 1
        print('Статискиа:', (window.score/window.total) * 100)
        print('Правильных ответов:', window.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_corecct('Неверно!')
            print('Статискиа:', (window.score/window.total) * 100)
            print('Правильных ответов:', window.score)

def next_question():
    num_question = randint(0, len(question_list) - 1)
    q = question_list[num_question]
    
    window.total += 1
    print('Всего воросов:', window.total)
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(click_OK)
next_question()
window.setLayout(layout_card)

window.show()
app.exec_()