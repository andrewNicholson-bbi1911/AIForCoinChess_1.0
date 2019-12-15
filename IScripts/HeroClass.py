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
        code = int(info[0])
        heroName = info[1]
        hp = int(info[2])
        damage = int(info[3])
        attackRange = int(info[4])
        attackSplashRadius = int(info[5])
        moveRange = int(info[6])
        spellID = int(info[7])

    def __init__(self, pattern):
        code = pattern.code
        heroName = pattern.heroName
        hp = pattern.hp
        damage = pattern.damage
        attackRange = pattern.attackRange
        attackSplashRadius = pattern.attackSplashRadius
        moveRange = pattern.moveRange
        spellID = pattern.spellID

    def __init__(self):
        code = 0

    #def changePosition(self, newCoords, flying)

    #def


