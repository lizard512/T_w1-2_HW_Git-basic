import requests

# 寶可夢資料來源
url = "https://pokeapi.co/api/v2/pokemon/pikachu"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    name = data["name"]
    stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}

    print(f"Pokémon Name: {name.capitalize()}")
    print("Stats:")
    for stat_name, stat_value in stats.items():
        print(f"  {stat_name.capitalize()}: {stat_value}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")