from pathlib import Path
import tkinter as tk
from tkinter import ttk

import requests

API_BASE_URL = "http://127.0.0.1:8000"
BACKGROUND = "white"
ASSET_FOLDER = Path(__file__).resolve().parent

CHARACTERS = {
    "Michael Jackson": {"image": "MJ.png", "endpoint": "/mj_quote"},
    "Eminem": {"image": "EMINEM.png", "endpoint": "/em_quote"},
    "Martin Luther King Jr.": {"image": "KING.png", "endpoint": "/mlk_quote"},
}


class QuoteApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Character Quotes")
        self.window.configure(bg=BACKGROUND)
        self.window.geometry("500x850")
        self.window.resizable(False, False)

        self.hide_job = None
        self.character_images = {
            name: tk.PhotoImage(file=ASSET_FOLDER / details["image"]).subsample(3, 3)
            for name, details in CHARACTERS.items()
        }
        self.quote_image = tk.PhotoImage(file=ASSET_FOLDER / "QUOTE.png")

        self.quote_canvas = tk.Canvas(
            self.window,
            width=300,
            height=414,
            bg=BACKGROUND,
            highlightthickness=0,
        )
        self.quote_canvas.pack(pady=(10, 0))

        self.character_button = tk.Button(
            self.window,
            command=self.show_random_quote,
            bg=BACKGROUND,
            activebackground=BACKGROUND,
            borderwidth=0,
            highlightthickness=0,
            cursor="hand2",
        )
        self.character_button.pack(pady=(0, 8))

        self.selected_character = tk.StringVar(value="Michael Jackson")
        self.character_menu = ttk.Combobox(
            self.window,
            textvariable=self.selected_character,
            values=list(CHARACTERS),
            state="readonly",
            justify="center",
            width=26,
            font=("Arial", 12),
        )
        self.character_menu.pack()
        self.character_menu.bind("<<ComboboxSelected>>", self.change_character)

        self.change_character()

    def change_character(self, _event=None):
        """Update the clickable portrait when the dropdown choice changes."""
        name = self.selected_character.get()
        self.character_button.configure(image=self.character_images[name])
        self.hide_quote()

    def show_random_quote(self):
        """Fetch and display a quote for the currently selected character."""
        name = self.selected_character.get()
        endpoint = CHARACTERS[name]["endpoint"]

        try:
            response = requests.get(f"{API_BASE_URL}{endpoint}", timeout=3)
            response.raise_for_status()
            data = response.json()
            quote = data["quote"]
        except (requests.RequestException, KeyError, ValueError):
            quote = "Could not reach the quote API. Start API.py with Uvicorn and try again."

        if self.hide_job is not None:
            self.window.after_cancel(self.hide_job)

        self.quote_canvas.delete("all")
        self.quote_canvas.create_image(150, 207, image=self.quote_image)
        text_id = self.quote_canvas.create_text(
            150,
            195,
            text=quote,
            width=225,
            justify="center",
            fill="#171717",
            font=("Arial", 16, "bold"),
        )
        self.fit_quote_text(text_id)
        self.hide_job = self.window.after(7000, self.hide_quote)

    def fit_quote_text(self, text_id):
        """Shrink long quotes until they fit safely inside the speech bubble."""
        font_size = 16
        while font_size > 10:
            bounds = self.quote_canvas.bbox(text_id)
            if bounds and bounds[2] - bounds[0] <= 225 and bounds[3] - bounds[1] <= 270:
                break
            font_size -= 1
            self.quote_canvas.itemconfigure(text_id, font=("Arial", font_size, "bold"))

    def hide_quote(self):
        """Hide both the speech bubble and its text."""
        if self.hide_job is not None:
            self.window.after_cancel(self.hide_job)
            self.hide_job = None
        self.quote_canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    QuoteApp(root)
    root.mainloop()
