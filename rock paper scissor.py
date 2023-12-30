from tkinter import *
from random import randint

def get_computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return choices[randint(0, 2)]

def update_user_choice(choice):
    user_entry.delete(0, END)
    user_entry.insert(0, choice)

def update_computer_choice(choice):
    comp_entry.delete(0, END)
    comp_entry.insert(0, choice)

def update_scores(winner):
    if winner == 'user':
        user_score['text'] = str(int(user_score['text']) + 1)
    elif winner == 'computer':
        comp_score['text'] = str(int(comp_score['text']) + 1)

def display_winner_message(message):
    final_message['text'] = message

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        display_winner_message("It's a Tie")
    elif (user_choice == 'rock' and computer_choice == 'scissor') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissor' and computer_choice == 'paper'):
        display_winner_message("User Wins")
        update_scores('user')
    else:
        display_winner_message("Computer Wins")
        update_scores('computer')

def button_clicked(user_choice):
    computer_choice = get_computer_choice()
    update_user_choice(user_choice)
    update_computer_choice(computer_choice)
    check_winner(user_choice, computer_choice)

def reset_game():
    user_score['text'] = '0'
    comp_score['text'] = '0'
    user_entry.delete(0, END)
    comp_entry.delete(0, END)
    final_message['text'] = ''

win = Tk()
win.geometry('700x500+400+150')
win.title('Rock Paper Scissor')
win.configure(bg='purple')

label_user = Label(win, text='USER', font='calibri 18 bold', width=8, bg='white', fg='black')
label_user.place(x=90, y=50)
label_comp = Label(win, text='COMPUTER', font='calibri 18 bold', width=11, bg='white', fg='black')
label_comp.place(x=420, y=50)
user_score = Label(win, text=0, font='calibri 18 bold', width=5, height=2, bg='white', fg='black')
user_score.place(x=110, y=130)
comp_score = Label(win, text=0, font='calibri 18 bold', width=5, height=2, bg='white', fg='black')
comp_score.place(x=460, y=130)

user_choice = Label(win, text='user choice', font='calibri 18 bold')
user_choice.place(x=30, y=230)
comp_choice = Label(win, text='comp choice', font='calibri 18 bold')
comp_choice.place(x=400, y=230)
user_entry = Entry(win, width=7, font='calibri 18', bd=2)
user_entry.place(x=160, y=230)
comp_entry = Entry(win, width=7, font='calibri 18', bd=2)
comp_entry.place(x=540, y=230)

final_message = Label(win, font='calibri 18 bold', bg='white', fg='black')
final_message.place(x=300, y=400)

btn_rock = Button(win, text='Rock', font='calibri 18 bold', width=7, bd=2, bg='orange', command=lambda: button_clicked('rock'))
btn_paper = Button(win, text='Paper', font='calibri 18 bold', width=7, bd=2, bg='green', command=lambda: button_clicked('paper'))
btn_scissor = Button(win, text='Scissor', font='calibri 18 bold', width=7, bd=2, bg='red', command=lambda: button_clicked('scissor'))

btn_reset = Button(win, text='Reset', font='calibri 18 bold', width=7, bd=2, bg='gray', command=reset_game)

label_user.place(x=90, y=50)
label_comp.place(x=420, y=50)
user_score.place(x=110, y=130)
comp_score.place(x=460, y=130)
user_choice.place(x=30, y=230)
comp_choice.place(x=400, y=230)
user_entry.place(x=160, y=230)
comp_entry.place(x=540, y=230)
final_message.place(x=300, y=400)

btn_rock.place(x=100, y=300)
btn_paper.place(x=280, y=300)
btn_scissor.place(x=460, y=300)
btn_reset.place(x=620, y=450)

win.mainloop()
