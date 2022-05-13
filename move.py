class Move:

    """
    A class that represents all aspects of a move
    """

    def __init__(self, hp: int, mp: int, damage: int, effect: str, hrestored: int, mrestored: int, name: str) -> None:
        """
        Sets up the move based on passed in parameter
        :param hp: the amount of HP is needed to use the move
        :param mp: the amount of MP is needed to cast the move
        :param damage: the amount of damage the move deals
        :param effect: the status effect the move can inflict
        :param hrestored: how much HP the move restores
        :param mrestored: how much MP the move restores
        :param name: the name of the move
        """
        self.move_hp_cost = hp
        self.move_mp_cost = mp
        self.move_damage = damage
        self.move_status_effect = effect
        self.move_hp_restored = hrestored
        self.move_mp_restored = mrestored
        self.move_name = name
