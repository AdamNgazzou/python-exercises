#ex8
def number_words(ch):
    count=1
    if(len(ch)==0):
        return 0
    while(ch.find(' ')!=-1):
        x=ch.find(' ')
        if(x!=len(ch)-1 and ch[x+1]!=' '):
            count+=1
        ch=ch[:x]+ch[x+1:]
    return count

print(number_words("adam is here  "))