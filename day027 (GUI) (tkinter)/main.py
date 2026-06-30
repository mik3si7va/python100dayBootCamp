import tkinter as tk

window = tk.Tk()
window.title("Miles -> Kilometers Converter")
window.geometry("300x150")


miles_label = tk.Label(window, text="Miles,", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=2, padx=10, pady=10)

kilometers = tk.Label(window, text="0", font=("Arial", 12, "bold"))
kilometers.grid(row=1, column=1, padx=10, pady=10)

km_label = tk.Label(window, text="Km.", font=("Arial", 12, "bold"))
km_label.grid(row=1, column=2, padx=10, pady=10)

equal_label = tk.Label(window, text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(row=1, column=0, padx=10, pady=10)


def add(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add(1, 2, 3, 4, 5))


def calculate(n, **kwargs):
    if "mult" in kwargs:
        n *= kwargs["mult"]
    if "add" in kwargs:
        n += kwargs["add"]
    return n


print(calculate(2, mult=5, add=3))


# entry widget
input = tk.Entry(window, width=10, justify="center")
input.grid(row=0, column=1, padx=10, pady=10)


def button_click():
    input_value = input.get()
    km_value = float(input_value) * 1.609
    kilometers.config(text=f"{km_value:.2f}")


button = tk.Button(window, text="Calculate", command=button_click)
button.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
