from bs4 import BeautifulSoup
from pathlib import Path
import lxml

# with open(Path(__file__).with_name("website.html")) as file:
#     content = file.read()


# soup = BeautifulSoup(content, "lxml")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.p)
# all_anchors = soup.find_all("a")
# print(all_anchors)

# for link in all_anchors:
#     print(link.get_text())
#     print(link.get("href"))

# headings = soup.find(name="h1", id="name")
# print(headings)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get_text())

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")

# print(headings)

import requests

# resposnse = requests.get("https://news.ycombinator.com")

# yc_page = resposnse.text

# soup = BeautifulSoup(yc_page, "html.parser")

# print(soup.title)

# all_anchor_stories = soup.select(selector=".titleline > a")
# all_scores = soup.select(selector=".score")
# str = []
# lnk = []
# upv = []

# for story in all_anchor_stories:
#     str.append(story.getText())
#     lnk.append(story.get("href"))

# for score in all_scores:
#     upv.append(int(score.getText().split()[0]))

# for n in range(len(str)):
#     print(f"{str[n]} with link {lnk[n]} has {upv[n]} upvotes")

# k = 0
# k_arg = 0
# for n in range(len(str)):
#     if upv[n] > k_arg:
#         k_arg = upv[n]
#         k = n

# print(max(upv))

# print(
#     f"The story with the most upvotes is {str[k]} with link {lnk[k]} and has {upv[k]} upvotes"
# )


# response = requests.get(
#     "https://www.empireonline.com/movies/features/best-movies-2/",
#     timeout=30,
# )
# response.raise_for_status()

with open(Path(__file__).with_name("empire.html")) as file:
    empire_page = file.read()

soup = BeautifulSoup(empire_page, "lxml")

list_of_movies = soup.select(selector="span h2 strong")

# print(list_of_movies)
list_of_movies.remove(list_of_movies[0])
list_of_movies.reverse()
list_FINAL = []
for movie in list_of_movies:
    list_number = int(movie.getText().split()[0][:-1])
    list_text = movie.getText().split()[1:]
    list_name = " ".join(list_text[0:-1])
    list_year = "".join(list_text[-1][-5:-1])
    if list_text[-1][-1] == ")":
        list_FINAL.append([list_number, (list_name), int(list_year)])

for movie in list_FINAL:
    print(f"{movie[0]} \t {movie[1]} - {movie[2]}")

with open(Path(__file__).with_name("movies.txt"), mode="w") as file:
    for movie in list_FINAL:
        file.write(f"{movie[0]} \t {movie[1]} \t {movie[2]}\n")
