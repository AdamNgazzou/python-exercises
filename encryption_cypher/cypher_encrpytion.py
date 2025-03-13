
def get_text():
    text = input("enter a word to encrypt : ")
    return text

def get_number():
    number = int(input("enrcyption pas : "))
    while (number >=26):
        number = int(input("enrcyption pas (number <26): "))
    return number
    
def encryption(text,number):
    new = ""
    for i in range(len(text)):
        if(text[i]!=" "):
            if(text[i]=="z" or text[i]=="Z"):
                new = new + chr(ord(text[i])-26+number)
            else:
                new = new + chr(ord(text[i])+number)
        else:
            new = new + text[i]
    return new     

def decryption(text,number):
    new = ""
    for i in range(len(text)):
        if(text[i]!=" "):
            if(text[i]==chr((ord("a")+number-1)) or text[i]==chr(ord("A")+number-1)):
                new = new + chr(ord(text[i])+26-number)
            else:
                new = new + chr(ord(text[i])-number)
        else:
            new = new + text[i]
    return new    
    
def read_file() :
    with open('file.txt', 'r') as input_file:
        content = input_file.read()
        return content

def dump_result(content):
    with open('file.txt', 'w') as output_file:
        # Write the content to the output file
        output_file.write(content)
    
def choose():
    choice = int(input("if you want to encrypt choose 1 if you want to decrypt choose 2"))
    while(choice!=1 and choice !=2):
        choice = int(input("if you want to encrypt choose 1 if you want to decrypt choose 2"))
    return choice


def main():
    number = get_number()
    text = read_file()

    if(choose()==1):
        print(text)
        encrypted_result = encryption(text,number)
        print(f"encrypted : {encrypted_result}")
        #dump
        dump_result(encrypted_result)
    else:
        print(text)
        decrypted_result = decryption(text,number)
        print(f"decrypted : {decrypted_result}")
        #dump
        dump_result(decrypted_result)

    
main()