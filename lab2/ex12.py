#ex12
def vowels(ch):
    x="aeouiy"
    t=''
    for char in ch :
        if(not(char in x)):
            t=t+char
    return t 
print(vowels('Heyy please help'))
            