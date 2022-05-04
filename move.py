class Move:
    def __init__(self, hp, mp, damage, effect, hrestored, mrestored, name):
        self.move_hp_cost = hp
        self.move_mp_cost = mp
        self.move_damage = damage
        self.move_status_effect = effect
        self.move_hp_restored = hrestored
        self.move_mp_restored = mrestored
        self.move_name = name
