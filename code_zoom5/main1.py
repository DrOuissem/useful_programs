#password

def test_number_characters(s,nb):
    return len(s)>nb

def test_special_character(s):
    return '_' in s or'-' in s
def test_number(s):
    if '0' in s or '1' in s or '2' in s or '3' in s or '4' in s or '5' in s or '6' in s or '7' in s or '8' in s or '9' in s:
        return True
    else:
        return False
def test_number2(s):
    for c in s:
        if c>='0' and c<='9':
            return True
    return False
def test_capital(s):
    for c in s:
        if c>='A' and c<='Z':
            return True
    return False
def test_small(s):
    for c in s:
        if c>='a' and c<='z':
            return True
    return False
repeat=True
while repeat:
    s = input("enter a password:")
    if test_number_characters(s,8) and test_special_character(s) and test_number2(s) and test_capital(s) and test_small(s):
        print("password accepted")
        repeat=False
    else:
        print("the password is not accepted")