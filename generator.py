import random, string


def generate(l=12, lc=True, uc=True, spc=True):
    
    if l < 4:
        print('Password has to be atleast 4 characters long.')
        l = 4
    
    pw_chars = [string.digits]
    
    if lc:
        pw_chars.append(string.ascii_lowercase)
    if uc:
        pw_chars.append(string.ascii_uppercase)
    if spc:
        pw_chars.append(string.punctuation)
        
    
        
    password = []
    for i in range(l):
        password.append(random.choice(''.join(pw_chars)))
    
    # Checks if any item in pw_char string set can be found in ur password
    # basically makes sure the password contains alteast one upper, lower, digits and special chars.

    v = len(pw_chars)
    for i in pw_chars:
        if not any(s in password for s in i):
            v += -1
            
    if v == len(pw_chars):
        return ''.join(password)
    else:
        return generate(l,lc,uc,spc)
        
