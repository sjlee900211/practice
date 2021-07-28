with open('myTextFile3.txt', 'w') as f:
    for num in range(1, 6):
        format_string = "3 x {0} = {1}\n".format(num, 3*num)
        f.write(format_string)