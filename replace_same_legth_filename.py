#filename = b'../../../../../../../../test.txt'
fakename = b'b/../bbbbbbbbbbbbbbbbbbbbbbb.txt'
filename = b'b/./bbbbbbbbbbbbbbbbbbbbbbbb.txt'
with open('aaaaaaaaaaaaaaaaaaaaaaaaaaaa.zip', mode='rb+') as f:
    b = f.read()
    try:
        b = b.replace(fakename, filename)
        f.seek(0)
        f.write(b)
    except ValueError:
        print("Error! Signature could not be found.")
