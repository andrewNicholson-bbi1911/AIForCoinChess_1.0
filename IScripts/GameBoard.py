from IScripts.Cell import Cell
from IScripts.Commands import Commands
from IScripts.HeroClass import Hero

class GameBoard:
    heroLibrary = []
    cellsOfBoard = []
    radiantHeroes = []
    dareHeroes = []

    def __init__(self, heroLibrary):
        self.heroLibrary = heroLibrary
        for i in range(1, 11, 1):
            for j in range(1, 11 - abs(6-i), 1):
                self.cellsOfBoard.append(Cell(i, j, self))
        for cell in self.cellsOfBoard:
            cell.setNeighbours()

    def addHero(self, newHero, isRadiant):
        if isRadiant:
            self.radiantHeroes.append(newHero)
        else:
            self.dareHeroes.append(newHero)

    def action(self, values):
        heroCoords = Commands.getCoordinates(values[0])
        actionID= int(values[1])
        activeCell = Cell()
        activeCell = self.cellOnBoardByCoords(heroCoords)
        if not activeCell == Cell():
            hero = activeCell.heroOnCell
            targetCell = Cell()
            targetCoords = []
            if actionID == 1:
                #MOVE
                activeCell.heroOnCell.changePosition(Commands.getCoordinates(values[2]), False)
            elif actionID == 2:
                #ATTACK
                targetCoords = Commands.getCoordinates(values[2])
                targetCell = self.cellOnBoardByCoords(targetCoords)
                if targetCell != Cell():
                    # the cell must be able for attack so I check it here;
                    centerTargetDistance = 6 - targetCell.position[1]
                    centerActiveDistance = 6 - activeCell.position[1]
                    xDistance = abs(targetCell.position[0]-activeCell.position[0])
                    if centerActiveDistance * centerTargetDistance < 0:
                        xDistance += centerActiveDistance if centerActiveDistance >= centerTargetDistance else centerTargetDistance
                    if xDistance <= hero.attackRange:
                        # if the cell is able for attack;
                        targetCell.setAbleToBeAttacked(hero.damage, hero.attackSplashRadius == 1)

            elif actionID == 3:
                #SHIFT COIN
                targetCoords = Commands.getCoordinates(values[2]);
                targetCell = self.cellOnBoardByCoords(targetCoords);
                if targetCell.heroOnCell != Hero() & activeCell.heroOnCell != Hero():
                    if len(activeCell.heroOnCell.code) > 1 and len(targetCell.heroOnCell.code) < 3:
                        coinSide = activeCell.heroOnCell.code % 10
                        activeCell.heroOnCell.code /= 10
                        targetCell.heroOnCell.code *= 10
                        targetCell.heroOnCell.code += coinSide
                        activeCell.heroOnCell.reinitialization()
                        targetCell.heroOnCell.reinitialization()

            elif actionID == 4:
                #CAST
                activeCell.heroOnCell.cast(Commands.getCoordinates(values[2]))


    def cellOnBoardByCoords(self,  position):
        for  cell in self.cellsOfBoard:
            if cell.position == position:
                return cell
        return Cell()
