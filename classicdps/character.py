""" Implementation of character stats. """
# pylint: disable=missing-class-docstring,missing-function-docstring,no-self-use
from skills import ALL_SKILLS
from collections import defaultdict

def load_config(config_path):
    pass

class Character:
    def __init__(self, stats_path):
        self.stats = load_config(stats_path)
        self.buffs = defaultdict(int)
        self.cooldowns = defaultdict(int)
        self.rage = 0

    def cast(self, skill, time):
        if self.cooldowns[skill] >= time:
            return 0
        dmg, cool_d, crit, rage = ALL_SKILLS[skill](self.stats, self.buffs, self.rage)
        self.cooldowns[skill] += cool_d
        self.rage += rage
        if crit:
            self.buffs["flurry"] = 3
        return dmg

if __name__ == "__main__":
    ch = Character("a")
    d = ch.cast("mh_attack", 1)
    print(d)
