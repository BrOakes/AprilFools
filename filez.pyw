import os

userhome = os.path.expanduser('~')
desktop = userhome + '\Desktop\\'

f = open('workfile', 'w')

i = 0
while i < 100:
    f = open(desktop + 'UMAD ' + str(i)+ '.txt', 'w')
    f.write("Hey, umad?")
    f.close()
        
    i += 1

print desktop
