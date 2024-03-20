# 1.Даны значения роста 20 юношей. Определить сколько юношей будут направлены
# в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).
import random

rost = [random.randint(170, 196) for _ in range(20)]

def is_basketball_player(player_height):
    return player_height > 190

basketball_players = list(filter(lambda r: is_basketball_player(r[1]), enumerate(rost, start=1)))
football_players = list(filter(lambda r: not is_basketball_player(r[1]), enumerate(rost, start=1)))

print("Результаты:")
print("Баскетбольная команда:")
for player in basketball_players:
    print(f"Игрок {player[0]} - {player[1]} см")

print("\nФутбольная команда:")
for player in football_players:
    print(f"Игрок {player[0]} - {player[1]} см")

print(f"Количество игроков в баскетбольной команде: {len(basketball_players)}")
print(f"Количество игроков в футбольной команде: {len(football_players)}")