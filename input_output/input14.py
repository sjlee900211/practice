f = open("two_times_table.txt")
lines = f.readlines()
f.close()
for line in lines:
    print(line, end="")