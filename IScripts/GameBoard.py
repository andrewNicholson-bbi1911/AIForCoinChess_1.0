from IScripts.Cell import Cell

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


#    def action(self, values):
#        heroCoords = Command.getCoordinates(values[0]);
#        byte
#        actionID = Byte.parseByte(values[1]);
#        ServerCell
#        activeCell = null;
#        activeCell = cellOnBoardByCoords(heroCoords);
#        if (activeCell != null){
#        HeroClass hero = activeCell.heroOnCell;
#        ServerCell targetCell;
#        byte[] targetCoords;
#        switch (actionID){
#        case 1://
#            MOVE
#        activeCell.heroOnCell.changePosition(Command.getCoordinates(values[2]), false);
#        break;
#        case
#        2: // ATTACK
#        targetCoords = Command.getCoordinates(values[2]);
#        targetCell = cellOnBoardByCoords(targetCoords);
#        if (targetCell != null){
#        // the cell must be able for attack so I check it here;
#        byte centerTargetDistance = (byte) ((byte)6 - targetCell.position[1]);
#        byte centerActiveDistance = (byte) ((byte)6 - activeCell.position[1]);
#        byte xDistance = (byte) (Math.abs(targetCell.position[0]-activeCell.position[0]));
#        if (centerActiveDistance * centerTargetDistance < 0){
#        xDistance += (centerActiveDistance >= centerTargetDistance)?centerTargetDistance:centerTargetDistance;
#        }
#        if (xDistance <= hero.attackRange){// if the cell is able for attack;
#        targetCell.setAbleToBeAttacked(hero.damage, hero.attackSplashRadius == 1);
#        } else {// the target cell is out of attack range;
#        throw e;
#        }
#
#        }
#        break;
#
#
#        case
#        3: // SHIFT
#        COIN
#        targetCoords = Command.getCoordinates(values[2]);
#        targetCell = cellOnBoardByCoords(targetCoords);
#        if (targetCell.heroOnCell != null & activeCell.heroOnCell != null) {
#        if (String.valueOf(activeCell.heroOnCell.code).length() > 1
#        & String.valueOf(targetCell.heroOnCell.code).length() < 3){
#        int coinSide = activeCell.heroOnCell.code % 10;
#        activeCell.heroOnCell.code /= 10;
#        targetCell.heroOnCell.code *= 10;
#        targetCell.heroOnCell.code += coinSide;
#        activeCell.heroOnCell.reinitialization();
#        targetCell.heroOnCell.reinitialization();
#        } else {
#        throw e;
#        }
#
#        } else {
#        throw e;
#        }
#        break;
#        case
#        4: // CAST
#        activeCell.heroOnCell.cast(Command.getCoordinates(values[2]));
#        break;
#        default:
#        throw
#        new
#        IllegalStateException("Unexpected value: " + actionID);
#        }
#        } else throw
#        e;
#        }