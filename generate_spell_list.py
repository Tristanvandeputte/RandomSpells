import random

arcane_conduit_table = [[5, 4, 0, 0, 0, 0, 0, 0, 0, 0], # 1
                        [5, 6, 0, 0, 0, 0, 0, 0, 0, 0], # 2
                        [5, 6, 2, 0, 0, 0, 0, 0, 0, 0], # 3
                        [6, 6, 4, 0, 0, 0, 0, 0, 0, 0], # 4
                        [6, 6, 4, 2, 0, 0, 0, 0, 0, 0], # 5
                        [6, 6, 4, 4, 0, 0, 0, 0, 0, 0], # 6
                        [6, 6, 4, 4, 2, 0, 0, 0, 0, 0], # 7
                        [6, 6, 4, 4, 4, 0, 0, 0, 0, 0], # 8
                        [6, 6, 4, 4, 4, 2, 0, 0, 0, 0], # 9
                        [7, 6, 4, 4, 4, 4, 0, 0, 0, 0], # 10
                        [7, 6, 4, 4, 4, 4, 2, 0, 0, 0], # 11
                        [7, 6, 4, 4, 4, 4, 4, 0, 0, 0], # 12
                        [7, 6, 4, 4, 4, 4, 4, 2, 0, 0], # 13
                        [7, 6, 4, 4, 4, 4, 4, 4, 0, 0], # 14
                        [7, 6, 4, 4, 4, 4, 4, 4, 2, 0], # 15
                        [7, 6, 4, 4, 4, 4, 4, 4, 4, 0], # 16
                        [7, 6, 4, 4, 4, 4, 4, 4, 4, 2], # 17
                        [7, 6, 5, 5, 4, 4, 4, 4, 4, 2], # 18
                        [7, 6, 5, 5, 5, 4, 4, 4, 4, 3], # 19
                        [7, 6, 5, 5, 5, 5, 4, 4, 4, 4]] # 20

def generate_spells(sorcerer_level):
    output = []
    print(f"Sorcerer level: {sorcerer_level} \n")

    for spell_level, number_of_spells in enumerate(arcane_conduit_table[sorcerer_level-1]):
        if number_of_spells == 0:
            break
        print(f"Level {spell_level} ({number_of_spells} spells)")
        output.append(f"Level {spell_level} ({number_of_spells} spells):\n")
        with open(f"level{spell_level}.txt", "r") as spell_level_file:
            spells = spell_level_file.readlines()
            for spell in random.sample(spells, number_of_spells):
                output.append(spell.strip() + '\n')
        output.append('\n')
    return "".join(output)

print(generate_spells(1))
