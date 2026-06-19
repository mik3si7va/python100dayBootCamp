import turtle

import prettytable

rainbow_colors = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"
]

# timmy = turtle.Turtle()
# timmy.color("chartreuse")
# timmy.pensize(5)
# timmy.speed(77)
# while True:
#     for color in rainbow_colors:
#         timmy.color(color)
#         timmy.circle(77)
#         timmy.right(7)

# screen = turtle.Screen()
# screen.exitonclick()

table = prettytable.PrettyTable()

table.field_names = ["pokemon", "type", "level"]
table.add_row(["Pikachu", "Electric", 5])
table.add_row(["Charmander", "Fire", 8])
table.add_row(["Bulbasaur", "Grass/Poison", 7])
table.add_row(["Squirtle", "Water", 6])

table.add_column("evolution", ["Raichu", "Charmeleon", "Ivysaur", "Wartortle"])

print(table)
table.align = "l"
print(table)