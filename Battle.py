class Battle:
    def __init__(self, hero, monster):
        # Assume creature1 is hero
        # Assume creature2 is monster
        self.hero = hero
        self.monster = monster
        self.damage1 = 0
        self.damage2 = 0
        self.won = 0 # No one wins
        self._fight()

    def _attack(self, attacker, defenser):
        damage = attacker.ATK - defenser.DEF
        if (damage < 0):
            damage = 0
        defenser.HP -= damage
        # Pass by ref, thus it works
        return damage

    def _fight(self):

        # Assume hero always fights first
        while (True):
            self.damage2 += self._attack(self.hero, self.monster)
            if (self.monster.isDead()):
                self.won = 1
                self.hero.getExp(self.monster.EXP)
                self.hero.getGold(self.monster.GLD)
                break
            self.damage1 += self._attack(self.monster, self.hero)
            if (self.hero.isDead()):
                self.won = 2
                break

            if (self.damage1 + self.damage2 == 0):
                # If they both cannot damage each other
                self.won = 3
                break
            # elif (self.damage1 == 0):
            #     # if monster cannot damage hero but hero can
            #     # Win directly
            #     self.won = 1
            
        if (self.won == 1):
            print('Hero won the battle, lost {0} HP, left {1} HP, gained {2} exp, gained {3} coins'.format(self.damage1, self.hero.HP, self.monster.EXP, self.monster.GLD))
        elif (self.won == 2):
            print('Hero failed and game is over')
        elif (self.won == 3):
            print('Cannot hurt each other')
        else:
            print('Illegal operation')
            
            
    # def _isBattleOver(self):
    #     return self.creature1.isDead() or self.creature2.isDead()

        