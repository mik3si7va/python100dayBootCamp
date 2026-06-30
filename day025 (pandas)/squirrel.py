import pandas
from os import path

# how many squirrels of each primary fur color are there in the data set?
directory = path.dirname(__file__)
data = pandas.read_csv(path.join(directory, "squirrel_data.csv"))
fur_color_counts = data["Primary Fur Color"].value_counts()


# change column name to "Fur Color" and "Count"
fur_color_counts = fur_color_counts.rename_axis("Fur Color")
fur_color_counts = fur_color_counts.reset_index(name="Count")


# create a new data frame from the fur color counts and save it to a new csv file
fur_color_counts_df = pandas.DataFrame(fur_color_counts)
fur_color_counts_df.to_csv(path.join(directory, "fur_color_counts.csv"))

print(fur_color_counts_df)
