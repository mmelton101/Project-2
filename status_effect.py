import random
rand = random


class StatusEffect:
    def set_status_effect(self, move):
        if move.move_status_effect != "None":
            num = rand.randint(0, 5)
            print(num)
            if num < 2:
                return move.move_status_effect
            else:
                return ""

    def continue_effect(self, status_effect):
        num = rand.randint(0, 4)
        print(num)
        if num < 3:
            return ""
        else:
            return status_effect
