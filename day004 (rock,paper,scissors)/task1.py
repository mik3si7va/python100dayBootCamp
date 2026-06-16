import random

# import module_1 

# randi = random.randint(1, 10)

# print(randi)

# print(module_1.fav_i)

# rand = random.random()
# print(rand)

# randf = random.uniform(1.0, 10.0)
# print(randf)
h=0
t=0
for i in range(1000):
    if random.random() < 0.5:
        h += 1
    else:
        t += 1
print(f"Heads: {h}, Tails: {t}")
