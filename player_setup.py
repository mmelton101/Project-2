import move as m


class PlayerSetup:
    def __init__(self):
        attack = m.Move(0, 0, 50, "None", 0, 0, "Attack")
        guard = m.Move(0, 0, 0, "None", 0, 0, "Guard")
        self.player_name = "You"
        self.player_move_list = [attack, guard]
        self.player_hp = 1000
        self.player_mp = 500

    def move_choice(self, move_selection):
        move_list = ["Firaga", "Sparkling Splash", "Pigeon Raid", "Cross Slash", "Curaga", "Stamina Spark"]
        if move_selection == "firaga":
            firaga = m.Move(0, 25, 50, "Burn", 0, 0, "Firaga")
            self.player_move_list.append(firaga)

        if move_selection == "sparkling splash":
            splash = m.Move(0, 25, 50, "Cold", 0, 0, "Sparkling Splash")
            self.player_move_list.append(splash)

        if move_selection == "pigeon raid":
            pigeon = m.Move(50, 0, 75, "None", 0, 0, "Pigeon Raid")
            self.player_move_list.append(pigeon)

        if move_selection == "cross slash":
            slash = m.Move(100, 0, 125, "Bleed", 0, 0, "Cross Slash")
            self.player_move_list.append(slash)

        if move_selection == "curaga":
            curaga = m.Move(0, 50, 0, "None", 1000, 0, "Curaga")
            self.player_move_list.append(curaga)

        if move_selection == "stamina spark":
            spark = m.Move(0, 3, 0, "None", 1000, 500, "Stamina Spark")
            self.player_move_list.append(spark)
