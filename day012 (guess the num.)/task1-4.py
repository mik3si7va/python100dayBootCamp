
game_level = 10

enemies = [
    "Goblin",
    "Troll",
    "Dragon",
    "Orc",
    "Vampire"
]

def create_enemy():
    if game_level < 5:
        return enemies[0]  # Goblin
    elif game_level < 10:
        return enemies[1]  # Troll
    elif game_level < 15:
        return enemies[2]  # Dragon
    elif game_level < 20:
        return enemies[3]  # Orc
    else:
        return enemies[4]  # Vampire
    
enemy = create_enemy()
print(f"An enemy has appeared: {enemy}")

enemies = 1

def incerement_enemies():
    enemies = 2
    print(f"Number of enemies inside function: {enemies}")
    
incerement_enemies()
print(f"Number of enemies outside function: {enemies}")


enemies = 1

def incerement_enemies():
    global enemies
    enemies += 1
    print(f"Number of enemies inside function: {enemies}")
    
incerement_enemies()
print(f"Number of enemies outside function: {enemies}")

PI = 3.14159

GOOGLE = "https://www.google.com"

def calculate_circumference(radius):
    return 2 * PI * radius

def open_google():
    print(f"Opening {GOOGLE}...")
    
print(calculate_circumference(5))
open_google()