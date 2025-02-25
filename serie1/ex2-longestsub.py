
ch=input("ch =")

def longestsub(ch):
    x=""
    res=""
    for i in range(len(ch)):
        for j in range(i,len(ch)):
            if(ch[j] in x):
                if(len(x) > len(res)):
                    
                    res=x
                x=""
            else:
                x=x+ch[j]
    return(res)

print(longestsub(ch))
                
        
