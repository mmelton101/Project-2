import random
rand = random


class StatusEffect:

    """
    Class that represents status effects and how they are applied and removed from characters
    """

    def set_status_effect(self, move) -> str:
        """
        Determines if the move has a status effect than determines if the status effect should be applied
        :param move: object that represents all the info a move has
        :return: the status effect of the move if it was applied or returns "" if the effect wasn't applied or if the move doesn't have one.
        """
        if move.move_status_effect != "None":
            num = rand.randint(0, 5)
            if num < 2:
                return move.move_status_effect
            else:
                return ""
        else:
            return ""

    def continue_effect(self, status_effect: str) -> str:
        """
        Determines if the the status effect should persist or if it should end
        :param status_effect: name of the status effect
        :return:
        """
        num = rand.randint(0, 4)
        if num < 3:
            return ""
        else:
            return status_effect
