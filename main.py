from tkinter import *
import json

###      --------      ADDONS IN THE FUTURE         ---------- ###
# add mistake finding
    # compare every letter to the original and add it to "mistakes" list
# add color highlighting (mistakes)
    # take every letter as itself and repaint... i guess... we'll see
# redesigning everything
    # button
    # entry
    # canvas
    # text style and presenting
    # resize
# update algorithm
# 
# but all of it later, yes, ok, i'm heading to the next one
# perhaps chess or game... that-like stuff makes me very excited!!  


# ---------------------- VARS --------------------- #
current_cpm = 0
max_cpm = 0
old_text = ''
FONT = ("Arial", 20)
timer = 0
welcome_txt = '''You have got 1 minute to test your speed.
Every minute the results are reset, so you'd better hurry...'''

with open('text.json', encoding='utf-8') as file:
    texts = json.load(file)

# --------------------- BRAIN --------------------- #

def start():
    start_stop.config(text='Type!', font=('italic'))
    start_stop['state'] = 'disabled'
    entry.focus()
    main_func()

def main_func():
    global max_cpm, current_cpm, old_text, timer
    canvas.itemconfig(print_text, text=texts['text1'])
    if len(old_text) > texts['text1']:
        # change the text
        pass
    text = entry.get()
    for letter in text:
        if letter == ' ':
            old_text += text
            entry.delete(0, END)
            max_label.config(text=f"{max_cpm} WPM")
            wpm_label.config(text=f"{current_cpm} WPM")
    timer += 10
    # every second
    if timer % 1000 == 0:
        timer_label.config(text=round(timer/1000))
    # every 10 seconds
    if timer % 10000 == 0:
        speed_check()
        current_cpm = 0
    # every minute 
    if timer % 60000 == 0:
        speed_check()
        current_cpm = 0
        timer = 0
        old_text = ''
    window.after(10, main_func)###########

def speed_check():
    global current_cpm, max_cpm
    # whole amount of chars over 5; how many 
    current_cpm = round(len(old_text)/5, 1)
    # if the speed increased
    if max_cpm < current_cpm:
        max_cpm = round(current_cpm, 1)

# ---------------------- GUI ---------------------- # 

window = Tk()
window.title('TypeTest')
window.minsize(900, 500)
window.config(padx=15, pady=15)

timer_label = Label(text=f"0", font=FONT)
timer_label.grid(column=1, row=0)

wpm_label = Label(text=f'{current_cpm} WPM')
wpm_label.grid(column=0, row=0)
max_label = Label(text=f'{max_cpm} WPM')
max_label.grid(column=2, row=0)

entry = Entry(width=30, font=("Courier", 15))
entry.grid(column=1, row=2)

canvas = Canvas(width=900, height=300, bg='pink', highlightthickness=0)
print_text = canvas.create_text(450, 150, text=welcome_txt, fill='white', width=500, font=FONT)
canvas.config()
canvas.grid(column=0, row=1, columnspan=3, pady=30)

start_stop = Button(text='Start', command=start, width=30, height=2)
start_stop.grid(column=1, row=3, pady=30)


window.mainloop()

