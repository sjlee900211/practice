f = open("two_times_table.txt")
for line in f.readlines():
    print(line, end="")
f.close()