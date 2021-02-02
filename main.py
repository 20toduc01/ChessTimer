from ChessTimer import ChessTimer
import threading, time
import tkinter as tk

def noUI():
    whiteName = input("Enter white player's name: ")
    blackName = input("Enter black player's name: ")
    timeLimit = int(input("Time limit in minutes: "))
    increment = int(input("Time increment in seconds: "))
    timer = ChessTimer(whiteName, blackName, timeLimit, increment)
    timer.startTimer()

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
    def getClockString(player):
        clock = player.clock
        if clock < 200:
            return f'{clock//600}:{(clock//10)%60}:{(clock%10)}'
        else:
            return f'{clock//600}:{(clock//10)%60}'

    def getClock(game):
        white = game.white
        black = game.black
        return (getClockString(white), getClockString(black))

    def updateClock():
        wc, bc = getClock(game)
        wClock['text'] = wc
        bClock['text'] = bc
        window.after(50, updateClock)

    def switchTurn(event):
        game.switchTurn()

    window = tk.Tk()
    # window.columnconfigure([0, 1], weight = 1, minsize = 300)
    # window.rowconfigure([0, 1], weight = 1, minsize = 150)
    # whiteNameLabel = tk.Label(master = window, text = game.white.name)
    # blackNameLabel = tk.Label(master = window, text = game.black.name)
    # whiteNameLabel.grid(row = 0, column = 0)
    # blackNameLabel.grid(row = 0, column = 1)
    window.columnconfigure(0, weight = 1, minsize = 250)
    window.rowconfigure([0, 1], weight = 1, minsize = 80)
    window.resizable(0, 0)
    whiteFrame = tk.Frame(master = window, bg = 'white')
    whiteFrame.grid(row = 0, column = 0, sticky = 'nesw')
    blackFrame = tk.Frame(master = window, bg = 'black')
    blackFrame.grid(row = 1, column = 0, sticky = 'nesw')

    wClock = tk.Label(master = whiteFrame, text = '0', bg = 'white', fg = 'black', font = ('Bahnschrift SemiBold', 44))
    bClock = tk.Label(master = blackFrame, text = '0', bg = 'black', fg = 'white', font = ('Bahnschrift SemiBold', 44))

    wClock.pack(side = tk.LEFT, padx=10)
    bClock.pack(side = tk.LEFT, padx=10)
    window.bind("<Key>", switchTurn)
    window.after(50, updateClock)
    window.mainloop()
    

getInput()
timer = ChessTimer("White", "Black", timeLimit, increment)
runThread = threading.Thread(target = timer.runTimer, args = (), daemon = True)
runThread.start()
run(timer)