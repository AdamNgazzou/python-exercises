#ex10
def pangram(ch):
    x="azertyuiopqsdfghjklmwxcvbn"
    for i in range(len(ch)):
        if(ch[i] in x):
            c=x.find(ch[i])
            x=x[:c]+x[c+1:]
    return len(x)==0

print(pangram("azertyuiopqsdfghjklmwxcvbn"))
print(pangram("azertyuiopqsdfghjklmwxcvb"))