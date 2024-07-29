import requests
from bs4 import BeautifulSoup

# First script simply hauls in all of the spells (make sure we're not fully dependant on the site)

response = requests.get('http://dnd5e.wikidot.com/spells')
soup = BeautifulSoup(response.content, "html.parser")
results = soup.find_all("table", {"class": "wiki-content-table"})
# Each table contains one spell level
for spell_level, spell_level_table in enumerate(results):
    with open(f"level{spell_level}.txt", "w") as spell_level_file:
        # special entries from oddysey
        if spell_level == 2:
            spell_level_file.write('Sleeping Draught | Enchantment | 1 Action | 60 feet | 1 minute | V, S, M\n')
        if spell_level == 3:
            spell_level_file.write('Animal Polymorph | Transmutation | 1 Action | 60 feet | Concentration, up to 10 minutes | V, S\n')
            spell_level_file.write('Fatebinding | Necromancy | 1 Action | 30 feet | 1 hour | V\n')
        if spell_level == 5:
            spell_level_file.write('Sword of Fate | Illusion | 1 Action | 60 feet | 1 hour | V\n')
        if spell_level == 6:
            spell_level_file.write('Seeds of Death | Necromancy | 1 Action | 30 feet | Concentration, up to 10 minutes | V, S, M\n')
        for i, row in enumerate(spell_level_table.find_all('tr')):
            # Ignore the header
            if i != 0:
                # [Name, School, casting time, range, duration, components]
                spell_details = [el.text.strip() for el in row.find_all('td')]
                if not "HB" in spell_details[0] and not "UA" in spell_details[0] and not "DC" in spell_details[1] and not "DG" in spell_details[1]:
                    spell_level_file.write(' | '.join(spell_details))
                    spell_level_file.write('\n')