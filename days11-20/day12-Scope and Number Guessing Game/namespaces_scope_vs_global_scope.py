# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")


# local Scope

# def drink_potion():
#     potion_strenght = 2
#     print(potion_strenght)
#
# drink_potion()


# global scope
# player_health = 10
#
#
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)
#
#     drink_potion()


game_level = 3
def create_enemy():
   enemies = ["Skeleton", "Zombie", "Alien"]
   if game_level < 5:
    new_enemy = enemies[0]

    print(new_enemy)

create_enemy()
