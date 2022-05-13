import move as m


class Player:

    """
    A class that contains all the information for the player
    """

    def __init__(self):
        """
        Creates all the moves that the player can select, set player HP and MP, and creates the player movelist
        """
        attack = m.Move(0, 0, 50, "None", 0, 0, "Attack")
        guard = m.Move(0, 0, 0, "None", 0, 0, "Guard")
        self.firaga = m.Move(0, 25, 50, "Burn", 0, 0, "Firaga")
        self.splash = m.Move(0, 25, 50, "Cold", 0, 0, "Sparkling Splash")
        self.pigeon = m.Move(50, 0, 75, "None", 0, 0, "Pigeon Raid")
        self.slash = m.Move(100, 0, 125, "Bleed", 0, 0, "Cross Slash")
        self.curaga = m.Move(0, 50, 0, "None", 1000, 0, "Curaga")
        self.spark = m.Move(0, 3, 0, "None", 1000, 500, "Stamina Spark")
        self.player_name = "You"
        self.player_move_list = [attack, guard]
        self.player_hp = 1000
        self.player_mp = 500

    def move_choice(self, move_selection: str) -> None:
        """
        Determines the name of the move the user selected and adds that move to the player list
        if it has not already been added to the movelist
        :param move_selection: name of the move the user selected
        """
        move_list = ["Firaga", "Sparkling Splash", "Pigeon Raid", "Cross Slash", "Curaga", "Stamina Spark"]

        if move_selection == "firaga" and self.firaga not in self.player_move_list:
            print("a")
            self.player_move_list.append(self.firaga)

        if move_selection == "sparkling splash" and self.splash not in self.player_move_list:
            self.player_move_list.append(self.splash)

        if move_selection == "pigeon raid" and self.pigeon not in self.player_move_list:
            self.player_move_list.append(self.pigeon)

        if move_selection == "cross slash" and self.slash not in self.player_move_list:
            self.player_move_list.append(self.slash)

        if move_selection == "curaga" and self.curaga not in self.player_move_list:
            self.player_move_list.append(self.curaga)

        if move_selection == "stamina spark" and self.spark not in self.player_move_list:
            self.player_move_list.append(self.spark)
