from IScripts.HeroClass import Hero
from IScripts.GameBoard import GameBoard


class Cell:
    neighbourCells = []
    position = []
    active = False
    ableToMove = False
    ableToCast = False
    heroOnCell = Hero()
    gameBoard = GameBoard()

    def __init__(self, raw, column, gameBoard):
        self.position = [raw, column]
        self.gameBoard = gameBoard
        return self

    def poseHero(self, hero):
        self.heroOnCell = hero

    def setNeighbours(self):
        if self.position[0] < 6:
            if self.position[0] == 1:
                if self.position[1] == 1:
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
                elif self.position[1] - 5 == self.position[0]:
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                else:
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
                self.neighbourCells.append((self.position[0] + 1, self.position[1]))
                self.neighbourCells.append((self.position[0] + 1, self.position[1] + 1))
            else:
                if self.position[1] == 1:
                    self.neighbourCells.append((self.position[0] - 1, self.position[1]))
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
                elif self.position[1] - 5 == self.position[0]:
                    self.neighbourCells.append((self.position[0] - 1, self.position[1] - 1))
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                else:
                    self.neighbourCells.append((self.position[0] - 1, self.position[1] - 1))
                    self.neighbourCells.append((self.position[0] - 1, self.position[1]))
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
                self.neighbourCells.append((self.position[0] + 1, self.position[1]))
                self.neighbourCells.append((self.position[0] + 1, self.position[1] + 1))
        elif self.position[0] > 6:
            if self.position[0] == 11:
                self.neighbourCells.append((self.position[0] - 1, self.position[1]))
                self.neighbourCells.append((self.position[0] - 1, self.position[1] + 1))
                if self.position[1] == 1:
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
                elif self.position[1] - 5 == self.position[0]:
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                else:
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
            else:
                if self.position[1] == 1:
                    self.neighbourCells.append((self.position[0] - 1, self.position[1]))
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
                elif self.position[1] - 5 == self.position[0]:
                    self.neighbourCells.append((self.position[0] - 1, self.position[1] - 1))
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                else:
                    self.neighbourCells.append((self.position[0] - 1, self.position[1] - 1))
                    self.neighbourCells.append((self.position[0] - 1, self.position[1]))
                    self.neighbourCells.append((self.position[0], self.position[1] - 1))
                    self.neighbourCells.append((self.position[0], self.position[1] + 1))
                self.neighbourCells.append((self.position[0] + 1, self.position[1]))
                self.neighbourCells.append((self.position[0] + 1, self.position[1] + 1))
        else:
            if self.position[1] == 1:
                self.neighbourCells.append((self.position[0] - 1, self.position[1]))
                self.neighbourCells.append((self.position[0], self.position[1] + 1))
                self.neighbourCells.append((self.position[0] + 1, self.position[1]))
            elif self.position[1] == 11:
                self.neighbourCells.append((self.position[0] - 1, self.position[1] - 1))
                self.neighbourCells.append((self.position[0], self.position[1] - 1))
                self.neighbourCells.append((self.position[0] + 1, self.position[1] - 1))
            else:
                self.neighbourCells.append((self.position[0] - 1, self.position[1]))
                self.neighbourCells.append((self.position[0] - 1, self.position[1] - 1))
                self.neighbourCells.append((self.position[0], self.position[1] + 1))
                self.neighbourCells.append((self.position[0] + 1, self.position[1]))
                self.neighbourCells.append((self.position[0] + 1, self.position[1] - 1))

    def setAbleToMove(self, rangeOfMove):
        self.removeAll()
        if self.heroOnCell != Hero() and rangeOfMove >= 0 and not self.ableToMove:
            self.ableToMove = True
            for neighbourCoords in self.neighbourCells:
                for cell in self.gameBoard.cellsOfBoard:
                    if cell.position == neighbourCoords:
                        if cell.heroOnCell == Hero():
                            cell.setAbleToMove(rangeOfMove - 1)
                        break

    def removeAll(self):
        self.active = False
        self.ableToMove = False
        self.ableToCast = False
