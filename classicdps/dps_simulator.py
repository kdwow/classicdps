


def sim(race, level):

    talents = load_config(talents_file)
    gear = load_config(gear_file)
    buffs = load_config(buffs_file)
    enemy = load_config(enemy_file)

    hero = init_hero(race, level, talents, gear, buffs)
    enemy = init_enemy(health, level, armor, resists)
    hero.target = enemy

    time = 0
    while True:

        damage += hero.mh_attack(time)
        damage += hero.oh_attack(time)
        damage += hero.cast_skill(time)






        time += 0.200
