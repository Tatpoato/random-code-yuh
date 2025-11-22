import requests

baseurl = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{baseurl}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data, error code: {response.status_code}")

def get_generation_info(species_url):
    response = requests.get(species_url)
    if response.status_code == 200:
        species_data = response.json()
        return species_data["generation"]["name"]
    else:
        print(f"Failed to get species data, error code: {response.status_code}")
        return "Unknown"

def get_damage_multipliers(types):
    type_multipliers = {}


    all_types = requests.get(baseurl + "type").json()["results"]
    for t in all_types:
        type_multipliers[t["name"]] = 1.0

    for type_info in types:
        type_url = type_info["type"]["url"]
        response = requests.get(type_url)
        if response.status_code != 200:
            continue
        data = response.json()
        relations = data["damage_relations"]

        for t in relations["double_damage_from"]:
            type_multipliers[t["name"]] *= 2
        for t in relations["half_damage_from"]:
            type_multipliers[t["name"]] *= 0.5
        for t in relations["no_damage_from"]:
            type_multipliers[t["name"]] *= 0

    return type_multipliers

def print_type_effectiveness(type_multipliers):
    weaknesses_2x = []
    weaknesses_4x = []
    resistances_0_5x = []
    resistances_0_25x = []
    immunities = []

    for t, multiplier in type_multipliers.items():
        if multiplier == 0:
            immunities.append(t)
        elif multiplier == 4:
            weaknesses_4x.append(t)
        elif multiplier == 2:
            weaknesses_2x.append(t)
        elif multiplier == 0.25:
            resistances_0_25x.append(t)
        elif multiplier == 0.5:
            resistances_0_5x.append(t)

    if weaknesses_4x:
        print("4x Weaknesses:")
        for t in weaknesses_4x:
            print(f"  - {t.capitalize()}")

    if weaknesses_2x:
        print("2x Weaknesses:")
        for t in weaknesses_2x:
            print(f"  - {t.capitalize()}")

    if resistances_0_25x:
        print("0.25x Resistances:")
        for t in resistances_0_25x:
            print(f"  - {t.capitalize()}")

    if resistances_0_5x:
        print("0.5x Resistances:")
        for t in resistances_0_5x:
            print(f"  - {t.capitalize()}")

    if immunities:
        print("Immunities:")
        for t in immunities:
            print(f"  - {t.capitalize()}")



pokename = input("Which pokemon?  ").lower().replace(" ", "-")
pokeinfo = get_pokemon_info(pokename)

if pokeinfo:
    weight = pokeinfo["weight"] / 10
    height = pokeinfo["height"] / 10

    print(f"\nName: {pokeinfo['name'].capitalize()}")
    print(f"Id: {pokeinfo['id']}")
    print(f"Weight: {weight}kg")
    print(f"Height: {height}m")

    # Generasjon
    species_url = pokeinfo["species"]["url"]
    generation = get_generation_info(species_url)
    gens = {
        "generation-i": "Gen 1", "generation-ii": "Gen 2", "generation-iii": "Gen 3",
        "generation-iv": "Gen 4", "generation-v": "Gen 5", "generation-vi": "Gen 6",
        "generation-vii": "Gen 7", "generation-viii": "Gen 8", "generation-ix": "Gen 9"
    }
    print(f"Generation: {gens.get(generation.lower(), generation.capitalize())}")

    # Type og svakheter
    types = pokeinfo["types"]
    type_names = [t["type"]["name"].capitalize() for t in types]
    print("Type(s):", ', '.join(type_names))

    print("\nType Effectiveness:")
    type_multipliers = get_damage_multipliers(types)
    print_type_effectiveness(type_multipliers)

    # Base stats
    print("\nBase Stats:")
    for stat in pokeinfo["stats"]:
        stat_name = stat["stat"]["name"].capitalize()
        stat_value = stat["base_stat"]
        print(f"  {stat_name}: {stat_value}")
hanuighighug = input("done??  ")
