""" Implementation of skill classes. """
# pylint: disable=missing-class-docstring,missing-function-docstring,no-self-use
import random

def mh_attack(stats, buffs, rage):
    base_dmg = random.uniform(stats["min_dmg"], stats["max_dmg"])
    ap_dmg = stats["atk_power"]*stats["atk_speed"]/14
    dmg = base_dmg + ap_dmg
    crit = False
    if random.random() < stats["crit"]:
        crit = True
        dmg *= 2
    atk_speed = stats["atk_speed"]*(1 - 0.3*bool(self.buffs["flurry"])
    rage = True
    return dmg, atk_speed, false, rage

def bloodthirst(stats):
    return 100

ALL_SKILLS = {
    "mh_attack": mh_attack,
    "bloodthirst": bloodthirst,
}
