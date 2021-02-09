import generator as g
import os, sys, subprocess

os.chdir(os.path.expanduser("~/Documents"))
cdir = os.getcwd()

app = input('Application: ')

if app == 'quit':
    sys.exit('Quitting...')
    
elif app == 'wipe':
    accept = input('Are you sure?\nThis will delete all your passwords! Y/N: ').lower()
    
    if accept == 'y':
        f = open('pwdb.csv', 'w')
        f.write('"source","ID","password"')
        f.close()
        sys.exit('Database wiped')
        
    else:
        sys.exit('Quitting...')

elif app == 'list':
    with open('pwdb.csv', mode='r') as f:
        for line in f:
            print(line)
    sys.exit('Done!')

name = input('Name or Email: ')

pw_len = int(input('Password length: '))

pw_special_chars = input('Special characters Y/N: ').lower()

if pw_special_chars == 'y':
    spc = 1
else:
    spc = 0
    
password = g.generate(pw_len,True,True,spc)
subprocess.run("pbcopy", universal_newlines=True, input=password)
print(f'Your password is: {password}\nCopied to clipboard!')

if not os.path.exists(os.getcwd()+'/pwdb.csv'):
    f = open('pwdb.csv', 'w')
    f.write('"source","ID","password"')
    f.close()


with open('pwdb.csv', mode='a', errors='ignore') as f:
    f.write(f'\n"{app}","{name}","{password}"')
    
