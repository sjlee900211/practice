f = open('two_times_table.txt', 'w')
for num in range(1,6):
    format_string = "2 x {0} = {1}\n".format(num, 2*num)
    f.write(format_string)
f.close()