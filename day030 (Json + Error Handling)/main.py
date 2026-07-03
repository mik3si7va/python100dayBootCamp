from os import path
import runpy


directory = path.dirname(__file__)
exercise2_main = path.join(directory, "exercise2", "main.py")

runpy.run_path(exercise2_main, run_name="__main__")
