import string
def rot13(message):
    Rot13 = ""
    alphabets = string.ascii_lowercase * 2 + string.ascii_uppercase * 2
    for i in message:
        if i in alphabets:
            Rot13 += alphabets[alphabets.index(i) + 13]
        else:
            Rot13 += i
    return Rot13


print(rot13("test"))
print(rot13("Test"))