class Hero:

    #basic stats about hero
    code = 0
    heroName = ""
    hp = 0
    damage = 0
    attackRange = 0
    attackSplashRadius = 0
    moveRange = 0
    spellID = 0

    #stats that would be change during game
    takenDamage = 0
    bonusDamage = 0
    bonusHP = 0

    radiantHero = True

    def __init__(self, info):
        self.code = int(info[0])
        self.heroName = info[1]
        self.hp = int(info[2])
        self.damage = int(info[3])
        self.attackRange = int(info[4])
        self.attackSplashRadius = int(info[5])
        self.moveRange = int(info[6])
        self.spellID = int(info[7])

    def __init__(self, pattern):
        self.code = pattern.code
        self.heroName = pattern.heroName
        self.hp = pattern.hp
        self.damage = pattern.damage
        self.attackRange = pattern.attackRange
        self.attackSplashRadius = pattern.attackSplashRadius
        self.moveRange = pattern.moveRange
        self.spellID = pattern.spellID

    def __init__(self):
        self.code = 0

    #def changePosition(self, newCoords, flying)

    #def


