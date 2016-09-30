import os, subprocess, random, time

fs = []

for file in os.listdir(os.getcwd()):
    if file.endswith(".pyw") and file != "controller.pyw":
        fs.append(file)

randlist = [25,100,150,200,250,300,360]

while True:
    
    f = random.choice(fs)
    execfile(f)
    time.sleep(random.choice(randlist))    
