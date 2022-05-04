class BossSetup:
    def __init__(self):
        self.boss_name = ""
        self.boss_move_list = []
        self.boss_hp = 0
        self.boss_mp = 0

    def boss_selection(self, boss_selection):
        print(boss_selection)
        if boss_selection == "sephiroth":
            self.boss_name = "Sephiroth"
            self.boss_hp = 1000
            self.boss_mp = 1000
            print(self.boss_name, self.boss_hp, self.boss_mp)

