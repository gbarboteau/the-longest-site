import string, random

def newURL():
    newURL = ''.join(random.choices(string.ascii_letters + string.digits, k=(random.randint(100, 150)))).lower()
    return newURL
