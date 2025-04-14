import random

string = "abcdefghijklmnopqrstuvwxyz123456789"
with open("file.txt", "w") as f:
    f.write("INSERT INTO temp (t, name) VALUES\n")
    for i in range (1,100000):
        name = string[random.randint(0, len(string)-1)] + string[random.randint(0, len(string)-1)] + string[random.randint(0, len(string)-1)]
        line = f"({i},'{name}')"
        if i != 99999:
            line+=',\n'
        else:
            line+=';\n'
        f.write(line)
