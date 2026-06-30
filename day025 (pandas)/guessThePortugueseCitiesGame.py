import turtle
import random
import tkinter as tk
import pandas as pd
from os import path
from PIL import Image

# Set up the screen
screen = turtle.Screen()
screen.title("Guess the Portuguese Cities Game")

image_path = path.join(path.dirname(__file__), "portDist.gif")  # Path to the image file

# Resize image to fit screen size
img = Image.open(image_path)
img_resized = img.resize((600, 800))
resized_path = path.join(path.dirname(__file__), "portDist_resized.gif")
img_resized.save(resized_path)

screen.addshape(resized_path)
screen.bgcolor("Black")
screen.setup(width=600, height=900)

turtle.shape(resized_path)


def top_left_textinput(title, prompt):
    """Show a text input dialog near the top-left corner of the turtle window."""
    root = screen.getcanvas().winfo_toplevel()
    root.update_idletasks()

    answer = {"value": None}

    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.resizable(False, False)
    dialog.transient(root)

    tk.Label(dialog, text=prompt, padx=12, pady=8).pack()
    entry = tk.Entry(dialog, width=35)
    entry.pack(padx=12, pady=(0, 8))

    buttons = tk.Frame(dialog)
    buttons.pack(pady=(0, 12))

    def submit():
        answer["value"] = entry.get()
        dialog.destroy()

    def cancel():
        dialog.destroy()

    tk.Button(buttons, text="OK", width=8, command=submit).pack(side="left", padx=4)
    tk.Button(buttons, text="Cancel", width=8, command=cancel).pack(side="left", padx=4)

    dialog.bind("<Return>", lambda event: submit())
    dialog.bind("<Escape>", lambda event: cancel())
    dialog.protocol("WM_DELETE_WINDOW", cancel)

    dialog.update_idletasks()
    x = root.winfo_rootx() + 10
    y = root.winfo_rooty() + 30
    dialog.geometry(f"+{x}+{y}")

    entry.focus_set()
    dialog.grab_set()
    root.wait_window(dialog)
    return answer["value"]


# # make the click on the screen return the coordinates of the click
# def get_click_coordinates(x, y):
#     print(f"Clicked at: ({x}, {y})")


# screen.onscreenclick(get_click_coordinates)

# getting the coordinates of the cities from the csv file
cities_data = pd.read_csv(path.join(path.dirname(__file__), "portDist.csv"))
print(cities_data)


## Create a turtle to write the city names
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# for index, row in cities_data.iterrows():
#     city_name = row["district"]
#     x_coord = row["x"]
#     y_coord = row["y"]

#     writer.goto(x_coord, y_coord)
#     writer.write(
#         city_name.replace(" ", "\n"), align="center", font=("Arial", 11, "bold")
#     )

corect_answers = []  # List to store correct answers

while True:
    answer_dist = top_left_textinput(
        title=f"{len(corect_answers)}/{len(cities_data)} Cities Correct",
        prompt="type de district's name (city) ('exit' to quit):",
    )
    if len(corect_answers) == len(cities_data):
        print("Congratulations! You guessed all the Portuguese districts!")
        break
    if answer_dist is None or answer_dist.lower() == "exit":
        break
    answer_dist = answer_dist.strip()  # Remove leading/trailing whitespace
    if answer_dist:
        answer_dist = answer_dist.lower()  # Convert the input to lowercase

        if answer_dist in cities_data["district"].str.lower().values:
            city_row = cities_data[
                cities_data["district"].str.lower() == answer_dist
            ].iloc[0]
            x_coord = city_row["x"]
            y_coord = city_row["y"]

            writer.goto(x_coord, y_coord)
            writer.write(
                answer_dist.title().replace(" ", "\n"),
                align="center",
                font=("Arial", 11, "bold"),
            )
            corect_answers.append(
                answer_dist.lower()
            )  # Add the correct answer to the list
        else:
            print(f"{answer_dist} is not a valid Portuguese district.")

    # Save the correct cities to a CSV file
    correct_cities = cities_data[
        cities_data["district"].str.lower().isin(corect_answers)
    ]
    correct_cities.to_csv(
        path.join(path.dirname(__file__), "correct_cities.csv"), index=False
    )

screen.bye()  # Close the turtle graphics window when the game ends
