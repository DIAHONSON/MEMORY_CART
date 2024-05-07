#создай приложение для запоминания информации     ;)
#виджеты :)
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QLabel,
    QVBoxLayout,QHBoxLayout,QRadioButton, QGroupBox,QButtonGroup,)

from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
#кодик;)
#part 1
app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Вопрос')

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('1')
rbtn_2 = QRadioButton('2')
rbtn_3 = QRadioButton('3')
rbtn_4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
#part 2
#БАНАНЧИКИ
#БАНАНЧИКИ
#БАНАНЧИКИ
#БАНАНЧИКИ
#панель резултата
AnsGroupBox = QGroupBox('результат теста')
lb_Result = QLabel("прав или не прав")
lb_Correct = QLabel("ответ тут")

layout_res=QVBoxLayout()
layout_res.addWidget(lb_Result,alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget (lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(layout_res)


#размещаем виджеты в окне
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox) 
layout_line2.addWidget(AnsGroupBox) 
AnsGroupBox.hide()
#RadioGroupBox.hide()
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)


layout_cart =QVBoxLayout()
layout_cart.addLayout(layout_line1, stretch = 2)
layout_cart.addLayout(layout_line2, stretch = 8)
layout_cart.addStretch(1)
layout_cart.addLayout(layout_line3, stretch = 1)
layout_cart.addStretch(1)
layout_cart.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def  check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')


def next_question():
    window.cur_question += 1
    if window.cur_question >= len(question_list):
        window.cur_question = 0 
    q = question_list[window.cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()






window = QWidget()
window.setLayout(layout_cart)
window.setWindowTitle('Memory Caed')

window.cur_question = -1

question_list = []


question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Итальянский', 'Испанский'))
question_list.append(Question('Какая порода собак чаще других пород используется на службе в армии, в полиции, для охраны государственных границ?', 'Немецкая овчарка', 'Чихуахуа', 'Боксер', 'Бульдог'))
question_list.append(Question('Чем киты кормят своих детенышей?', 'Молоком', 'Кальмарами', 'Планктоном', 'Рыбой'))
question_list.append(Question('Луйши футболист', 'Месси', 'Рональдо', 'Неимар', 'мне пофек'))
question_list.append(Question('Какова была профессия тех, кто первым начал носить помпон на зимней шапке?', 'моряки', 'воспитатели', 'повара', 'артисты'))
question_list.append(Question('Для чего нужны кольца на банках с газировкой?', 'фиксировать трубочку', ' так удобнее открывать', 'чтобы ставить банки друг на друга', 'так проще ухватиться за открывашку'))
question_list.append(Question('Слабое место Ахилеса?', 'Пятка', 'Глаз', 'Горло', 'Колено'))
question_list.append(Question('Какое самое ядовитое животное?', 'Медуза', 'Лягуха', 'Змея', 'Злая учительница в школе'))
question_list.append(Question('Самая богатая компания', 'Apple', 'Microsoft', 'Amazon', 'Продуктовый магазин в деревне'))
question_list.append(Question('Мое любимое число?', '28', '33', '96', 'у меня его нет'))
question_list.append(Question('Какая страна является самой маленькой в мире?', 'Ватикан', 'Монако', 'Мальдивы', 'Мальта'))
question_list.append(Question('Сколько белых квадратов на шахматной доске?', '64', '34', '16', '32'))
question_list.append(Question('Сколько зубов у здоровго человека?', '32', '28', '24', '20'))
question_list.append(Question('Какой самый просматриваемый ролик на Ютубе?', 'Baby shark dance', 'Despacito', 'See you again', '250 тысяч тонн тро....'))
question_list.append(Question('Вам понравилась викторина', 'Кто такая викторина?', 'ДА', 'НЕЕ', 'Бананчики'))


btn_OK.clicked.connect(click_OK)
window.resize(400,300)
next_question()

window.show()
#БАНАНЧИКИ
app.exec()
#part 3 

