import time, os, threading, msvcrt, sys

class Player(object):
    def __init__(self):
        self.name = ''
        self.piece = ''
        self.timeRemain = 0

    def __init__(self, name, piece, timeLimit):
        self.name = name
        self.piece = piece
        self.clock = timeLimit


class ChessTimer(object):
    def __init__(self, whiteName, blackName, timeLimit, increment):
        self.white = Player(whiteName, 'white', timeLimit*600)
        self.black = Player(blackName, 'black', timeLimit*600)
        self.increment = increment*10
        self.turn = 'white'

    def drawTimer(self, white, black):
        os.system('cls')
        print(f'{white.name} : {white.clock//600}:{(white.clock//10)%60}:{(white.clock%10)}')
        print(f'{black.name} : {black.clock//600}:{(black.clock//10)%60}:{(black.clock%10)}')

    
    def switchTurn(self):
        if self.turn == 'white':
            self.turn = 'black'
            self.white.clock += self.increment
        else: 
            self.turn = 'white'
            self.black.clock += self.increment
    
    def runTimer(self):
        white = self.white
        black = self.black
        while white.clock*black.clock != 0:
            # playerInterrupt = threading.Thread(target = keyboardInterrupt, args = (), daemon = True)
            # playerInterrupt.start()
            time.sleep(0.089) # FIX LATER
            if self.turn == 'white':
                white.clock -= 1
            else:
                black.clock -= 1
            self.drawTimer(white, black)
            
        if white.clock == 0:
            print(f'{white.name} lost on time')
        else:
            print(f'{black.name} lost on time')


if __name__ == "__main__":
    timeLimit = int(input("Time: "))
    increment = int(input("Inc: "))
    ChessTimer("White", "Black", timeLimit, increment).runTimer()
    time.sleep(100000)