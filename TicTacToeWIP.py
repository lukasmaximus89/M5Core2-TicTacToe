from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

line0 = M5Line(x1=0, y1=80, x2=320, y2=80, color=0x000, width=1, parent=None)
line1 = M5Line(x1=0, y1=161, x2=320, y2=161, color=0x000, width=1, parent=None)
line2 = M5Line(x1=106, y1=0, x2=107, y2=240, color=0x000, width=1, parent=None)
line3 = M5Line(x1=213, y1=0, x2=214, y2=240, color=0x000, width=1, parent=None)
touch_button0 = M5Btn(text='', x=1, y=4, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button1 = M5Btn(text='', x=110, y=4, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button2 = M5Btn(text='', x=219, y=4, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button3 = M5Btn(text='', x=219, y=85, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button4 = M5Btn(text='', x=110, y=85, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button5 = M5Btn(text='', x=1, y=85, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button6 = M5Btn(text='', x=1, y=168, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button7 = M5Btn(text='', x=110, y=168, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
touch_button8 = M5Btn(text='', x=219, y=168, w=100, h=70, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_28, parent=None)
label0 = M5Label('Text', x=70, y=100, color=0xff0000, font=FONT_MONT_48, parent=None)
label0.set_hidden(True)


from numbers import Number

def Check():
  global noughtsorcross, turns
  if turns > 0 and turns % 2 == 1:
    noughtsorcross = 'X'
  elif turns % 2 == 0:
    noughtsorcross = 'O'

def touch_button0_pressed():
  global noughtsorcross, turns
  Check()
  touch_button0.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button0.pressed(touch_button0_pressed)

def touch_button5_pressed():
  global noughtsorcross, turns
  Check()
  touch_button5.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button5.pressed(touch_button5_pressed)

def touch_button1_pressed():
  global noughtsorcross, turns
  Check()
  touch_button1.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button1.pressed(touch_button1_pressed)

def touch_button6_pressed():
  global noughtsorcross, turns
  Check()
  touch_button6.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button6.pressed(touch_button6_pressed)

def touch_button2_pressed():
  global noughtsorcross, turns
  Check()
  touch_button2.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button2.pressed(touch_button2_pressed)

def touch_button7_pressed():
  global noughtsorcross, turns
  Check()
  touch_button7.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button7.pressed(touch_button7_pressed)

def touch_button3_pressed():
  global noughtsorcross, turns
  Check()
  touch_button3.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button3.pressed(touch_button3_pressed)

def touch_button8_pressed():
  global noughtsorcross, turns
  Check()
  touch_button8.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button8.pressed(touch_button8_pressed)

def touch_button4_pressed():
  global noughtsorcross, turns
  Check()
  touch_button4.set_btn_text(noughtsorcross)
  turns = (turns if isinstance(turns, Number) else 0) + 1
  pass
touch_button4.pressed(touch_button4_pressed)

turns = 0
noughtsorcross = ''

def Clear():
    touch_button0.set_btn_text('')
    touch_button1.set_btn_text('')
    touch_button2.set_btn_text('')
    touch_button3.set_btn_text('')
    touch_button4.set_btn_text('')
    touch_button5.set_btn_text('')
    touch_button6.set_btn_text('')
    touch_button7.set_btn_text('')
    touch_button8.set_btn_text('')

def Owins():
  label0.set_hidden(False)
  label0.set_text('O wins')
  wait_ms(2000)
  label0.set_hidden(True)
  Clear()

def Xwins():
  label0.set_hidden(False)
  label0.set_text('X wins')
  wait_ms(2000)
  label0.set_hidden(True)
  Clear()

while True:
  if touch_button0.btn_text == "O" and touch_button4.btn_text == "O" and touch_button8.btn_text == "O":
      Owins()
  elif touch_button0.btn_text == "O" and touch_button1.btn_text == "O" and touch_button2.btn_text == "O":
      Owins()
  elif touch_button5.btn_text == "O" and touch_button4.btn_text == "O" and touch_button3.btn_text == "O":
      Owins()
  elif touch_button6.btn_text == "O" and touch_button7.btn_text == "O" and touch_button8.btn_text == "O":
      Owins()
  elif touch_button0.btn_text == "O" and touch_button5.btn_text == "O" and touch_button6.btn_text == "O":
      Owins()
  elif touch_button1.btn_text == "O" and touch_button4.btn_text == "O" and touch_button7.btn_text == "O":
      Owins()
  elif touch_button2.btn_text == "O" and touch_button3.btn_text == "O" and touch_button8.btn_text == "O":
      Owins()
  elif touch_button6.btn_text == "O" and touch_button4.btn_text == "O" and touch_button2.btn_text == "O":
      Owins()
  elif touch_button0.btn_text == "X" and touch_button4.btn_text == "X" and touch_button8.btn_text == "X":
      Xwins()
  elif touch_button0.btn_text == "X" and touch_button1.btn_text == "X" and touch_button2.btn_text == "X":
      Xwins()
  elif touch_button5.btn_text == "X" and touch_button4.btn_text == "X" and touch_button3.btn_text == "X":
      Xwins()
  elif touch_button6.btn_text == "X" and touch_button7.btn_text == "X" and touch_button8.btn_text == "X":
      Xwins()
  elif touch_button0.btn_text == "X" and touch_button5.btn_text == "X" and touch_button6.btn_text == "X":
      Xwins()
  elif touch_button1.btn_text == "X" and touch_button4.btn_text == "X" and touch_button7.btn_text == "X":
      Xwins()
  elif touch_button2.btn_text == "X" and touch_button3.btn_text == "X" and touch_button8.btn_text == "X":
      Xwins()
  elif touch_button6.btn_text == "X" and touch_button4.btn_text == "X" and touch_button2.btn_text == "X":
      Xwins()
