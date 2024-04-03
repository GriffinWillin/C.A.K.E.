from random import choice
letters = ["a","b","c","d","e","f","g"]

def Monster(how):
    out = []
    x = 0
    while(x<how):
        out.append(choice(letters))
        x+= 1
    return out



# According to all known laws of aviation, bees should not be able to fly.
# =======
print(Monster(50))

