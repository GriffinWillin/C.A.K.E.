from random import choice
letters = ["a","b","c","d","e","f","g"]

def BROTHER(how):
    out = []
    x = 0
    while(x<how):
        out.append(choice(letters))
        x+= 1
    return out

print(BROTHER(50))