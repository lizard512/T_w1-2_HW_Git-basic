import requests

def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError:
        print(f"Error: Pokémon '{pokemon_name}' not found.")
        data = None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        data = None
    else:
        print(f"Successfully retrieved data for Pokémon '{pokemon_name}'.")
    finally:
        print("Execution completed.")
    return data

# 測試以驗證錯誤處理的結果
pokemon_name = "pikachu"
print(f"Retrieving data for Pokémon '{pokemon_name}':")
data = get_pokemon_data(pokemon_name)
if data:
    print(data)

pokemon_name = "invalid_pokemon"
print(f"\nRetrieving data for Pokémon '{pokemon_name}':")
data = get_pokemon_data(pokemon_name)
if data:
    print(data)
