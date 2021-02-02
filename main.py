from ChessTimer import ChessTimer
import threading, time

def noUI():
    whiteName = input("Enter white player's name: ")
    blackName = input("Enter black player's name: ")
    timeLimit = int(input("Time limit in minutes: "))
    increment = int(input("Time increment in seconds: "))
    timer = ChessTimer(whiteName, blackName, timeLimit, increment)
    timer.startTimer()

import tkinter as tk

'''
window = tk.Tk()
greeting = tk.Label(text = 'Hello World', fg = 'white', bg = 'black', width = 40, height = 20)
greeting.pack()

button = tk.Button(text = "Click me!", width = 25, height = 5, bg = "blue", fg = "yellow")
button.pack()

entry = tk.Entry()
entry.pack()

window.mainloop()

import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


window.mainloop()

import tkinter as tk

window = tk.Tk()
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=10, pady=10)



window.mainloop()


import tkinter as tk
import random

def rollDice():
    result = random.randint(1, 6)
    resultLabel['text'] = str(result)


window = tk.Tk()
window.columnconfigure(0, weight = 1, minsize = 200)
window.rowconfigure([0, 1], weight = 1, minsize = 100)
resultLabel = tk.Label(master = window, text = '0')
rollButton = tk.Button(master = window, text = 'Roll me', command = rollDice)
rollButton.grid(row = 0, column = 0, sticky = 'nsew')
resultLabel.grid(row = 1, column = 0, sticky = 'nsew')
window.mainloop()
'''

timeLimit = 10
increment = 0

def getInput():
    import tkinter as tk

    def setEntryText(entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)

    def setTimeLimit():
        try:
            global timeLimit
            timeLimit = int(timeInput.get())
        except:
            setEntryText(timeInput, timeLimit)
    
    def setIncrement():
        try:
            global increment
            increment = int(incInput.get())
        except:
            setEntryText(incInput, increment)

    def destroyWindow():
        window.destroy()


    window = tk.Tk()
    window.columnconfigure([0, 1], weight = 1, minsize = 100)
    window.columnconfigure(2, weight = 1, minsize = 50)
    window.rowconfigure([0, 1, 2], weight = 1, minsize = 50)
    
    timeLabel = tk.Label(master = window, text = 'Time limit: ')
    timeLabel.grid(row = 0, column = 0, sticky = 'w')
    timeInput = tk.Entry(master = window, text = '10')
    timeInput.grid(row = 0, column = 1, sticky = 'w')
    timeSubmit = tk.Button(master = window, text = 'Set', command = setTimeLimit)
    timeSubmit.grid(row = 0, column = 2)

    incLabel = tk.Label(master = window, text = 'Increment: ')
    incLabel.grid(row = 1, column = 0, sticky = 'w')
    incInput = tk.Entry(master = window, text = '0')
    incInput.grid(row = 1, column = 1, sticky = 'w')
    incSubmit = tk.Button(master = window, text = 'Set', command = setIncrement)
    incSubmit.grid(row = 1, column = 2)
    
    submit = tk.Button(master = window, text = 'OK', command = destroyWindow)
    submit.grid(row = 2, column = 0, sticky = 'ew')

    submit = tk.Button(master = window, text = 'Exit', command = exit, width = 11)
    submit.grid(row = 2, column = 1,)
    window.mainloop()

def run(game):
    def getClock(game):
        white = game.white
        black = game.black
        return (f'{white.clock//600}:{(white.clock//10)%60}:{(white.clock%10)}',
        f'{black.clock//600}:{(black.clock//10)%60}:{(black.clock%10)}')

    def updateClock():
        wc, bc = getClock(game)
        wClock['text'] = wc
        bClock['text'] = bc
        window.after(1000, updateClock)

    def switchTurn(event):
        game.switchTurn()

    window = tk.Tk()
    window.columnconfigure([0, 1], weight = 1, minsize = 300)
    window.rowconfigure([0, 1], weight = 1, minsize = 150)

    whiteNameLabel = tk.Label(master = window, text = game.white.name)
    blackNameLabel = tk.Label(master = window, text = game.black.name)
    whiteNameLabel.grid(row = 0, column = 0)
    blackNameLabel.grid(row = 0, column = 1)
    wClock = tk.Label(master = window, text = '0')
    bClock = tk.Label(master = window, text = '0')
    wClock.grid(row = 1, column = 0)
    bClock.grid(row = 1, column = 1)
    window.bind("<Key>", switchTurn)
    window.after(1000, updateClock)
    window.mainloop()
    

getInput()
timer = ChessTimer("White", "Black", timeLimit, increment)
runThread = threading.Thread(target = timer.runTimer, args = (), daemon = True)
runThread.start()
run(timer)