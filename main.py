from ChessTimer import ChessTimer
from config import *
import threading, time
import tkinter as tk

timeLimit = 10
increment = 0

def getInput():
    def setEntryText(entry, text):
        entry.delete(0, tk.END)
        entry.insert(0, text)

    def submitInput():
        try:
            global timeLimit
            global increment
            timeLimit = int(timeInput.get())
            increment = int(incInput.get())
            window.destroy()
        except:
            setEntryText(timeInput, timeLimit)
            setEntryText(incInput, increment)


    window = tk.Tk()
    window.title('Setup')
    window.resizable(0, 0)
    window.iconbitmap(ICON)
    window.columnconfigure([0, 1], weight = 1, minsize = 100)
    window.rowconfigure([0, 1, 2], weight = 1, minsize = 50)
    
    timeLabel = tk.Label(master = window, text = 'Time limit')
    timeLabel.grid(row = 0, column = 0, sticky = 'news')
    timeInput = tk.Entry(master = window, width=5)
    setEntryText(timeInput, timeLimit)
    timeInput.grid(row = 0, column = 1, sticky = 'w')

    incLabel = tk.Label(master = window, text = 'Increment')
    incLabel.grid(row = 1, column = 0, sticky = 'news')
    incInput = tk.Entry(master = window, width=5)
    setEntryText(incInput, increment)
    incInput.grid(row = 1, column = 1, sticky = 'w')
    
    submit = tk.Button(master = window, text = 'OK', command = submitInput)
    submit.grid(row = 2, column = 0, sticky = 'ew')

    submit = tk.Button(master = window, text = 'Exit', command = exit)
    submit.grid(row = 2, column = 1, sticky = 'ew')
    window.mainloop()


def run():
    def getClockString(player):
        clock = player.clock
        minute = clock//600
        second = (clock//10)%60
        milisec = clock%10
        if second < 10: second = '0' + str(second)
        if clock < 200:
            return f'{minute}:{second}:{milisec}'
        else:
            return f'{minute}:{second}'

    def getClock():
        white = timer.white
        black = timer.black
        return (getClockString(white), getClockString(black))

    def updateClock():
        wc, bc = getClock()
        wClock['text'] = wc
        bClock['text'] = bc
        window.after(50, updateClock)

    def switchTurn(event):
        timer.switchTurn()


    timer = ChessTimer("White", "Black", timeLimit, increment)
    runThread = threading.Thread(target = timer.runTimer, args = (), daemon = True)
    runThread.start()

    window = tk.Tk()
    window.iconbitmap(ICON)
    window.title('Clock')
    window.columnconfigure(0, weight = 1, minsize = 250)
    window.rowconfigure([0, 1], weight = 1, minsize = 80)
    window.resizable(0, 0)

    whiteFrame = tk.Frame(master = window, bg = 'white')
    whiteFrame.grid(row = 0, column = 0, sticky = 'nesw')
    wClock = tk.Label(master = whiteFrame, text = '0', bg = 'white', fg = 'black', font = ('Bahnschrift SemiBold', 44))
    wClock.pack(side = tk.LEFT, padx=10)

    blackFrame = tk.Frame(master = window, bg = 'black')
    blackFrame.grid(row = 1, column = 0, sticky = 'nesw')
    bClock = tk.Label(master = blackFrame, text = '0', bg = 'black', fg = 'white', font = ('Bahnschrift SemiBold', 44))
    bClock.pack(side = tk.LEFT, padx=10)
    
    window.bind("<Key>", switchTurn)
    window.after(50, updateClock)
    window.mainloop()


getInput()
run()