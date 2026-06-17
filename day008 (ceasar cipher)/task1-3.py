def greet():
    print("statement 1")
    print("statement 2")
    print("statement 3")
    
greet()

def sum (one, two):
    return one + two

print(sum(2,3))
print(sum(4,5))

def greetings_loved_ones(where, how ,when):
    print(f"meet me at the {where}, {how} at {when}")
    
greetings_loved_ones('teather', 'behind stage', 'midnight')
greetings_loved_ones(when = 'midnight', how = 'behind stage', where = 'teather')