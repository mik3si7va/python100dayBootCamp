from fastapi import FastAPI
import random

app = FastAPI()

MJ_quotes = [
    "Lies run sprints, but the truth runs marathons.",
    "The greatest education in the world is watching the masters at work.",
    "If you enter this world knowing you are loved and leave knowing the same, then everything that happens in between can be dealt with.",
    "Please go for your dreams. Whatever your ideals, you can become whatever you want to become.",
    "To give someone a piece of your heart is worth more than all the wealth in the world.",
    "In a world filled with hate, we must still dare to hope.",
    "The meaning of life is contained in every single expression of life.",
]

EM_quotes = [
    "You only get one shot, do not miss your chance to blow.",
    "The truth is you don't know what is going to happen tomorrow. Life is a crazy ride, and nothing is guaranteed.",
    "Success is my only option, failure's not.",
    "Everybody has goals, aspirations, or whatever, and everybody has been at a point in their life where nobody believed in them.",
    "You can make something of your life. It just depends on your drive.",
    "Trust is hard to come by. That's why my circle is small and tight.",
    "Somewhere deep down there's a decent man in me; he just can't be found.",
]

KING_quotes = [
    "The time is always right to do what is right.",
    "Faith is taking the first step even when you don't see the whole staircase.",
    "Darkness cannot drive out darkness; only light can do that.",
    "Injustice anywhere is a threat to justice everywhere.",
    "We must accept finite disappointment, but never lose infinite hope.",
    "Life's most persistent and urgent question is: What are you doing for others?",
    "Intelligence plus character, that is the goal of true education.",
]


@app.get("/mj_quote")
def get_mj_quote():
    return {"author": "Michael Jackson", "quote": random.choice(MJ_quotes)}


@app.get("/em_quote")
def get_em_quote():
    return {"author": "Eminem", "quote": random.choice(EM_quotes)}


@app.get("/mlk_quote")
def get_king_quote():
    return {"author": "Martin Luther King Jr.", "quote": random.choice(KING_quotes)}
