import random
from status_effect import StatusEffect
se = StatusEffect()


class MoveProcessor:

    """
    a class that process the moves of both the player and boss
    """

    def __init__(self):
        """
        Sets up needed variables needed to accurately calculate damage and for the boss to choose a move
        """
        self.player_guard = 1
        self.boss_guard = 1
        self.boss_move_count = 0
        self.boss_move = ""
        self.text = ""
        self.brass_knuckles = 1
        self.player_status_effect = ""
        self.boss_status_effect = ""

    def player_move(self, player, player_move: str, boss) -> bool and str:
        self.text = ""
        for move in player.player_move_list:
            if move.move_name == player_move:
                player_move = move

        if self.player_status_effect == "Petrify" or self.player_status_effect == "Confusion":
            if self.player_status_effect == "Petrify":
                self.player_status_effect = se.continue_effect(self.player_status_effect)
                return f"{player.player_name} couldn't move because you were petrified."
            else:
                self.player_status_effect = se.continue_effect(self.player_status_effect)
                return f"{player.player_name} couldn't move because you were confused."

        if player_move.move_name == "Guard":
            self.player_guard = 2
            self.boss_guard = 1
            return True, f"{player.player_name} used {player_move.move_name}."

        if player_move.move_name == "Stamina Spark" and player_move.move_mp_cost > 0:
            player_move.move_mp_cost = player_move.move_mp_cost - 1
            player.player_hp = 1000
            player.player_mp = 500
            self.boss_guard = 1
            self.text = f"{player.player_name} used {player_move.move_name} and was completely revitalized. You have {player_move.move_mp_cost} left."
            return True, self.text

        if player_move.move_name == "Stamina Spark" and player_move.move_mp_cost <= 0:
            self.boss_guard = 1
            self.text = f"{player.player_name} ran out of {player_move.move_name}."
            return False, self.text

        if player_move.move_name == "Curaga" and player_move.move_mp_cost <= player.player_mp:
            player.player_mp = player.player_mp - player_move.move_mp_cost
            player.player_hp = player.player_hp + player_move.move_hp_restored
            if player.player_hp > 1000:
                player.player_hp = 1000
            self.boss_guard = 1
            self.text = f"{player.player_name} used {player_move.move_name}. {player.player_name} regained {player_move.move_hp_restored} HP."
            return True, self.text

        if player_move.move_hp_cost < player.player_hp and player_move.move_mp_cost == 0:
            player.player_hp = player.player_hp - player_move.move_hp_cost
            boss.boss_hp = boss.boss_hp - (player_move.move_damage / self.boss_guard)

            if self.boss_status_effect == "":
                self.boss_status_effect = se.set_status_effect(player_move)
                if self.boss_status_effect != "":
                    self.text = f"{boss.boss_name} was inflicted with {self.boss_status_effect}\n"

            self.text = self.text + f"{player.player_name} used {player_move.move_name}. Dealt {player_move.move_damage / self.boss_guard} damage"
            self.boss_guard = 1
            return True, self.text

        elif player_move.move_mp_cost <= player.player_mp and player_move.move_hp_cost == 0 and player_move.move_hp_restored == 0:
            player.player_mp = player.player_mp - player_move.move_mp_cost
            boss.boss_hp = boss.boss_hp - (player_move.move_damage / self.boss_guard)

            if self.boss_status_effect == "":
                self.boss_status_effect = se.set_status_effect(player_move)
                if self.boss_status_effect != "":
                    self.text = f"{boss.boss_name} was inflicted with {self.boss_status_effect}\n"

            self.text = self.text + f"{player.player_name} used {player_move.move_name}. Dealt {player_move.move_damage / self.boss_guard} damage"
            self.boss_guard = 1
            return True, self.text

        else:
            self.boss_guard = 1
            if player_move.move_hp_cost != 0:
                self.text = f"{player.player_name} don't have enough HP to use {player_move.move_name}"
                return False, self.text
            else:
                self.text = f"{player.player_name} don't have enough MP to cast {player_move.move_name}"
                return False, self.text

    def boss_turn(self, boss, player) -> bool and str:
        """
        Decides what boss AI should be called based on which boss is selected
        :param boss: object with all the info the boss has
        :param player: object with all the info the player has
        :return: returns the text that will be printed to the screen and whether the boss turn has ended or not
        """
        if boss.boss_name == "Sephiroth":
            turn_end, text = self.sephiroth_move_selection(boss, player)
            return turn_end, text
        else:
            turn_end, text = self.tendo_move_selection(boss, player)
            return turn_end, text

    def sephiroth_move_selection(self, boss, player) -> bool and str:
        """
        AI the boss uses to decide what move it will use for its turn and then uses the move
        :param boss: object with all the info the boss has
        :param player: object with all the info the player has
        :return: returns the text that will be printed to the screen and whether the boss turn has ended or not
        """
        self.text = ""
        if self.boss_move_count == 6:
            self.boss_move_count = 0

        if self.boss_status_effect == "Cold":
            self.boss_status_effect = se.continue_effect(self.boss_status_effect)
            return False, f"{boss.boss_name} caught a cold and couldn't move.\n"
        elif self.boss_status_effect == "Burn":
            self.boss_status_effect = se.continue_effect(self.boss_status_effect)
            boss.boss_hp = boss.boss_hp - 50
            self.text = f"{boss.boss_name} was burned and took 50 damage.\n"
        elif self.boss_status_effect == "Bleed":
            self.boss_status_effect = se.continue_effect(self.boss_status_effect)
            boss.boss_hp = boss.boss_hp - 100
            self.text = f"{boss.boss_name} started to bleed and took 100 damage.\n"

        if self.boss_move_count == 0:
            self.boss_move_count += 1
            self.boss_guard = 2
            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[0].move_name} and Guarded himself for 3 turns."
            self.player_guard = 1
            return False, self.text
        elif self.boss_move_count == 1:
            self.boss_move_count += 1
            self.boss_guard = 2
            player.player_hp = player.player_hp - (boss.boss_move_list[1].move_damage / self.player_guard)
            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[1].move_name}. {boss.boss_name} dealt {boss.boss_move_list[1].move_damage / self.player_guard} damage"
            self.player_guard = 1
            return False, self.text
        elif self.boss_move_count == 2:
            self.boss_move_count += 1
            self.boss_guard = 2
            player.player_hp = player.player_hp - (boss.boss_move_list[2].move_damage / self.player_guard)
            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[2].move_name}. {boss.boss_name} dealt {boss.boss_move_list[2].move_damage / self.player_guard} damage"
            self.player_guard = 1
            return False, self.text
        elif self.boss_move_count == 3:
            self.boss_move_count += 1
            player.player_hp = player.player_hp - (boss.boss_move_list[3].move_damage / self.player_guard)
            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[3].move_name}. {boss.boss_name} dealt {boss.boss_move_list[3].move_damage / self.player_guard} damage"
            self.player_guard = 1
            return False, self.text
        elif self.boss_move_count == 4:
            self.boss_move_count += 1
            player.player_hp = player.player_hp - (boss.boss_move_list[4].move_damage / self.player_guard)

            if self.player_status_effect == "":
                self.player_status_effect = se.set_status_effect(boss.boss_move_list[4])
                if self.player_status_effect != "":
                    self.text = f"{player.player_name} were inflicted with {self.boss_status_effect}\n"

            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[4].move_name}. {boss.boss_name} dealt {boss.boss_move_list[4].move_damage / self.player_guard} damage"
            self.player_guard = 1
            return False, self.text
        elif self.boss_move_count == 5 and boss.boss_hp > 250:
            self.boss_move_count += 1
            player.player_hp = player.player_hp - (boss.boss_move_list[5].move_damage / self.player_guard)

            if self.player_status_effect == "":
                self.player_status_effect = se.set_status_effect(boss.boss_move_list[5])
                if self.player_status_effect != "":
                    self.text = f"{player.player_name} were inflicted with {self.boss_status_effect}\n"

            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[5].move_name}. {boss.boss_name} dealt {boss.boss_move_list[5].move_damage / self.player_guard} damage"
            self.player_guard = 1
            return False, self.text
        elif self.boss_move_count == 5 and boss.boss_hp <= 250:
            self.boss_move_count += 1
            player.player_hp = 1
            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[6].move_name} and set your HP to 1."
            player.player_hp = 1
            self.player_guard = 1
            return False, self.text

    def tendo_move_selection(self, boss, player) -> bool and str:
        """
        AI the boss uses to decide what move it will use for its turn and then uses the move
        :param boss: object with all the info the boss has
        :param player: object with all the info the player has
        :return: returns the text that will be printed to the screen and whether the boss turn has ended or not
        """
        self.text = ""
        if self.boss_move_count == 4:
            self.boss_move_count = 0

        if self.boss_status_effect == "Cold":
            self.boss_status_effect = se.continue_effect(self.boss_status_effect)
            return False, f"{boss.boss_name} caught a cold and couldn't move.\n"
        elif self.boss_status_effect == "Burn":
            self.boss_status_effect = se.continue_effect(self.boss_status_effect)
            boss.boss_hp = boss.boss_hp - 50
            self.text = f"{boss.boss_name} was burned and took 50 damage.\n"
        elif self.boss_status_effect == "Bleed":
            self.boss_status_effect = se.continue_effect(self.boss_status_effect)
            boss.boss_hp = boss.boss_hp - 100
            self.text = f"{boss.boss_name} started to bleed and took 100 damage.\n"

        if boss.boss_hp <= 500 and self.brass_knuckles == 1:
            self.brass_knuckles = 1.5
            self.text = self.text + f"{boss.boss_name} equipped brass knuckles. Now all of {boss.boss_name}'s  attack will deal more damage."
            self.player_guard = 1
            return False, self.text

        if self.boss_move_count == 0:
            self.boss_move_count += 1
            player.player_hp = player.player_hp - ((boss.boss_move_list[0].move_damage / self.player_guard) * self.brass_knuckles)
            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[0].move_name} and hit you with string of sweeping punches. {boss.boss_name} dealt {(boss.boss_move_list[0].move_damage / self.player_guard) *self.brass_knuckles} damage"
            self.player_guard = 1
            return False, self.text

        elif self.boss_move_count == 1:
            self.boss_move_count += 1
            player.player_hp = player.player_hp - ((boss.boss_move_list[1].move_damage / self.player_guard) * self.brass_knuckles)
            self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[1].move_name}. {boss.boss_name} dealt {(boss.boss_move_list[1].move_damage / self.player_guard) * self.brass_knuckles} damage"
            self.player_guard = 1
            return False, self.text

        elif self.boss_move_count == 2:
            self.boss_move_count += 1
            self.text = self.text + f"{boss.boss_name} is engulfed by a golden aura and is charged up for a devastating blow."
            self.player_guard = 1
            return False, self.text

        elif self.boss_move_count == 3:
            if boss.boss_hp <= 500:
                rand = random
                num = rand.randint(2, 4)
                if num == 2:
                    self.boss_move_count += 1
                    player.player_hp = player.player_hp - ((boss.boss_move_list[2].move_damage / self.player_guard) * self.brass_knuckles)
                    self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[2].move_name} and descended on you with the power of a dragon. {boss.boss_name} dealt {(boss.boss_move_list[2].move_damage / self.player_guard) * self.brass_knuckles} damage"
                    self.player_guard = 1
                    return False, self.text
                elif num == 3:
                    self.boss_move_count += 1
                    if self.player_guard == 1:
                        player.player_hp = 0
                        self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[3].move_name} and struck your heart killing you instantly."
                    else:
                        player.player_hp = player.player_hp - ((300 / self.player_guard) * self.brass_knuckles)
                        self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[3].move_name}, but you guarded so {boss.boss_name} barely missed your heart. {boss.boss_name} dealt {(300 / self.player_guard) * self.brass_knuckles} damage"
                    self.player_guard = 1
                    return False, self.text
                else:
                    self.boss_move_count += 1
                    player.player_hp = player.player_hp - ((boss.boss_move_list[4].move_damage / self.player_guard) * self.brass_knuckles)
                    self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[4].move_name}. {boss.boss_name} dealt {(boss.boss_move_list[4].move_damage / self.player_guard) * self.brass_knuckles} damage"
                    self.player_guard = 1
                    return False, self.text
            else:
                self.boss_move_count += 1
                player.player_hp = player.player_hp - ((boss.boss_move_list[2].move_damage / self.player_guard) * self.brass_knuckles)
                self.text = self.text + f"{boss.boss_name} used {boss.boss_move_list[2].move_name} and descended on you with the power of a dragon. {boss.boss_name} dealt {(boss.boss_move_list[2].move_damage / self.player_guard) * self.brass_knuckles} damage"
                self.player_guard = 1
                return False, self.text
