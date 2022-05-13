import move as m


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
            self.boss_mp = "???"

            wall = m.Move(0, 0, 0, "None", 0, 0, "Wall")
            self.boss_move_list.append(wall)

            flare = m.Move(0, 0, 150, "None", 0, 0, "Shadow Flare")
            self.boss_move_list.append(flare)

            attack = m.Move(0, 0, 50, "None", 0, 0, "Attack")
            self.boss_move_list.append(attack)

            pale = m.Move(0, 0, 100, "None", 0, 0, "Pale Horse")
            self.boss_move_list.append(pale)

            super_ = m.Move(0, 0, 200, "Confusion", 0, 0, "Super Nova")
            self.boss_move_list.append(super_)

            break_ = m.Move(0, 0, 50, "Petrify", 0, 0, "Break")
            self.boss_move_list.append(break_)

            angel = m.Move(0, 0, 0, "None", 0, 0, "Heartless Angel")
            self.boss_move_list.append(angel)

        if boss_selection == "tendo":
            self.boss_name = "Tendo"
            self.boss_hp = 1000
            self.boss_mp = 0

            beatdown = m.Move(0, 0, 100, "None", 0, 0, "Royal Beatdown")
            self.boss_move_list.append(beatdown)

            finish = m.Move(0, 0, 100, "None", 0, 0, "Relentless Finish")
            self.boss_move_list.append(finish)

            descent = m.Move(0, 0, 200, "None", 0, 0, "Dragon's Descent")
            self.boss_move_list.append(descent)

            right_hand = m.Move(0, 0, 0, "None", 0, 0, "God's Right Hand")  # will immediately kill if not guarded
            self.boss_move_list.append(right_hand)

            left_wing = m.Move(0, 0, 250, "None", 0, 0, "Devil's Left Wing")
            self.boss_move_list.append(left_wing)
