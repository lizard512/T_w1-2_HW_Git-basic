import pandas as pd

# 建立一個寶可夢數據的 DataFrame
data = {
    "Name": ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"],
    "Type": ["Grass/Poison", "Fire", "Water", "Electric"],
    "HP": [45, 39, 44, 35],
    "Attack": [49, 52, 48, 55],
    "Defense": [49, 43, 65, 40]
}

df = pd.DataFrame(data)
print("Pokémon DataFrame:")
print(df)

# 計算平均 HP
average_hp = df["HP"].mean()
print("\nAverage HP:", average_hp)

# 新增一列，計算戰鬥力
df["Power"] = df["HP"] + df["Attack"] + df["Defense"]
print("\nDataFrame with Power:")
print(df)