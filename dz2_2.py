
with open("1.txt") as f:
    len_text1 = len(f.readlines())

with open("2.txt") as f:
    len_text2 = len(f.readlines())

with open("1.txt") as f:
    data1 = f.read()

with open("2.txt") as f:
    data2 = f.read()

with open("result.txt", "w") as f:
    if len_text1 > len_text2:
        f.write("2.txt\n")
        f.write(f'{str(len_text2)}\n')
        f.write(f'{data2}\n')
        f.write("1.txt\n")
        f.write(f'{str(len_text1)}\n')
        f.write(data1)

    else:
        f.write("1.txt\n")
        f.write(f'{str(len_text1)}\n')
        f.write(f'{data1}\n')
        f.write("2.txt\n")
        f.write(f'{str(len_text2)}\n')
        f.write(data2)


