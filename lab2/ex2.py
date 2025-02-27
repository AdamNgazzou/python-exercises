def is_palindrome(ch):
    for i in range(len(ch)//2):
        if (ch[i]!=ch[len(ch)-i-1]):
            return False
    return True

print(is_palindrome('hex'))
print(is_palindrome("traart"))