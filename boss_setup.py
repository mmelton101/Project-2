class BossSetup:
    def __init__(self):
        self.boss_name = ""
        self.boss_move_list = []
        self.boss_hp = 0
        self.boss_mp = 0

    def boss_selection(self, boss_selection):
        if boss_selection == "sephiroth":
            self.boss_name = "Sephiroth"
            self.boss_hp = 1000
            self.boss_mp = 1000

        if boss_selection == "tendo":
            self.boss_name = "Tendo"
            self.boss_hp = 1000
            self.boss_mp = 500
