import os

def identifycss():
    cwd = os.getcwd()
    for file in os.listdir(cwd):
        if file.endswith(".css"):
            return file

file = identifycss()

def readfile():
    f = open(file, 'r')
    css = str(f.read())
    css = ''.join(css.split())
    f.close()
    return css

css = readfile()
if file.endswith(".css"):
    file = file[:-4]
f = open(file + ".min.css", 'w')
f.write(css)


