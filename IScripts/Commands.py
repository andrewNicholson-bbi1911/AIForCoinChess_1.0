class Commands:
    strartGame = "!S"
    radiant = "R"
    dare = "D"
    turn = "T"
    missTurn = "Ms"
    endGame = "E"
    win = "W!"
    lose = "L!"
    noScore = "0!"
    error = "er"
    notEnoughCoins = "nec"
    impossibleAction = "ia"
    wrongCoords = "wc"
    busyCell = "bc"
    wrongID = "wid"
    giveUpReason = "G"
    disconnectReason = "_D"
    noConnectedReason = "_NC!"
    pose = "P"
    move = "M"
    shift = "S"
    cast = "C"
    attack = "A"
    Diclaim = "rej"

    def getCoordinates(self, coords_str):
        coordsN = coords_str.split(";")
        intCoords = [int(coordsN[0]), int(coordsN[1])]
        return intCoords

    def setCoords(self, coords_int):
        coords_str = str(coords_int[0]) + ";" + str(coords_int[1])
        return (coords_str)
