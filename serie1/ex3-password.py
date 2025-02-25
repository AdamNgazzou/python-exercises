def valid_password(ch):
    number_test=False
    lower_test=False
    upper_test=False
    special_test=False
    x="azertyuiopqsdfghjklmwxcvbn"
    special_case = "!@#$%^&*()-_=+|[]{};:/?.>"
    for char in ch :
        if(char in x) :
            lower_test=True
        if(char in x.upper()):
            upper_test=True
        if(char in "1234567890"):
            number_test=True
        if(char in special_case):
            special_test=True
    return (lower_test and upper_test and number_test and len(ch)>=8 and special_test)
 
 
password=input("ch =")
while(not(valid_password(password))):
    password=input("ch =")


        
